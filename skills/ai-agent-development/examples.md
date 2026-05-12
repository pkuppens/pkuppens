# AI Agent Development — Examples

Python and C# code examples for common agent patterns. Companion to [SKILL.md](SKILL.md).

## Python examples

### 1. Minimal chat completion agent

No framework required — just the `openai` SDK (works with OpenAI and Ollama):

```python
from openai import OpenAI

def create_agent(
    base_url: str = "http://localhost:11434/v1",
    model: str = "llama3.2",
    system_prompt: str = "You are a helpful assistant.",
) -> callable:
    """Create a simple chat completion agent.

    Args:
        base_url: LLM API endpoint. Use Ollama for on-premises.
        model: Model identifier.
        system_prompt: System instructions for the agent.

    Returns:
        callable: A function that takes a user message and returns a response.
    """
    client = OpenAI(base_url=base_url, api_key="not-needed")

    def chat(user_message: str) -> str:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
        )
        return response.choices[0].message.content

    return chat


agent = create_agent()
print(agent("What is retrieval-augmented generation?"))
```

### 2. Tool-using agent with provider abstraction

Framework-free implementation with swappable providers:

```python
import json
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from openai import OpenAI


@dataclass
class ToolResult:
    name: str
    result: str


@dataclass
class AgentResponse:
    content: str
    tools_called: list[ToolResult] = field(default_factory=list)
    model: str = ""
    total_tokens: int = 0


class BaseLLMProvider(ABC):
    """Abstract LLM provider — swap implementations without changing agent code."""

    @abstractmethod
    def complete_with_tools(
        self,
        messages: list[dict],
        tools: list[dict],
        max_iterations: int = 5,
    ) -> AgentResponse:
        ...


class OpenAICompatibleProvider(BaseLLMProvider):
    """Provider for OpenAI-compatible APIs (OpenAI, Ollama, vLLM)."""

    def __init__(self, base_url: str, model: str, api_key: str = "not-needed"):
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.model = model

    def complete_with_tools(
        self,
        messages: list[dict],
        tools: list[dict],
        max_iterations: int = 5,
    ) -> AgentResponse:
        tools_called = []
        total_tokens = 0

        for _ in range(max_iterations):
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools if tools else None,
            )
            msg = response.choices[0].message
            total_tokens += response.usage.total_tokens if response.usage else 0

            if not msg.tool_calls:
                return AgentResponse(
                    content=msg.content or "",
                    tools_called=tools_called,
                    model=self.model,
                    total_tokens=total_tokens,
                )

            messages.append(msg.model_dump())

            for tool_call in msg.tool_calls:
                result = self._execute_tool(
                    tool_call.function.name,
                    json.loads(tool_call.function.arguments),
                )
                tools_called.append(ToolResult(tool_call.function.name, result))
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": result,
                })

        return AgentResponse(
            content="Max iterations reached.",
            tools_called=tools_called,
            model=self.model,
            total_tokens=total_tokens,
        )

    def _execute_tool(self, name: str, arguments: dict) -> str:
        """Override or register tool handlers."""
        return json.dumps({"error": f"Unknown tool: {name}"})


def create_provider(backend: str, **kwargs) -> BaseLLMProvider:
    """Factory for creating LLM providers by backend name.

    Args:
        backend: Provider identifier ("ollama", "openai", "azure").
        **kwargs: Provider-specific configuration.

    Returns:
        BaseLLMProvider: Configured provider instance.

    Raises:
        ValueError: If the backend is not recognised.
    """
    providers = {
        "ollama": lambda: OpenAICompatibleProvider(
            base_url=kwargs.get("base_url", "http://localhost:11434/v1"),
            model=kwargs.get("model", "llama3.2"),
        ),
        "openai": lambda: OpenAICompatibleProvider(
            base_url="https://api.openai.com/v1",
            model=kwargs.get("model", "gpt-4o"),
            api_key=kwargs["api_key"],
        ),
    }
    if backend not in providers:
        raise ValueError(f"Unknown backend: {backend}. Available: {list(providers)}")
    return providers[backend]()
```

### 3. RAG agent with LangChain

```python
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser


def build_rag_chain(
    pdf_path: str,
    collection_name: str = "docs",
    llm_model: str = "gpt-4o",
):
    """Build a RAG chain from a PDF document.

    Args:
        pdf_path: Path to the PDF file to index.
        collection_name: Chroma collection name.
        llm_model: LLM model identifier.

    Returns:
        A runnable chain that answers questions from the PDF.
    """
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=64,
    )
    chunks = splitter.split_documents(docs)

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=OpenAIEmbeddings(),
        collection_name=collection_name,
    )
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "Answer the question based on the provided context. "
            "If the context does not contain the answer, say so.\n\n"
            "Context:\n{context}"
        )),
        ("user", "{question}"),
    ])

    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | ChatOpenAI(model=llm_model)
        | StrOutputParser()
    )
    return chain
```

### 4. Multi-agent with LangGraph

```python
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI


class AgentState(TypedDict):
    task: str
    research: str
    draft: str
    review: str
    final: str


def researcher(state: AgentState) -> dict:
    """Research agent gathers information about the task."""
    llm = ChatOpenAI(model="gpt-4o")
    result = llm.invoke(
        f"Research the following topic thoroughly:\n{state['task']}"
    )
    return {"research": result.content}


def writer(state: AgentState) -> dict:
    """Writer agent creates a draft from research findings."""
    llm = ChatOpenAI(model="gpt-4o")
    result = llm.invoke(
        f"Write a clear document based on this research:\n{state['research']}"
    )
    return {"draft": result.content}


def reviewer(state: AgentState) -> dict:
    """Reviewer agent provides feedback on the draft."""
    llm = ChatOpenAI(model="gpt-4o")
    result = llm.invoke(
        f"Review this draft for accuracy and clarity:\n{state['draft']}"
    )
    return {"review": result.content}


def build_multi_agent_graph() -> StateGraph:
    """Build a research-write-review multi-agent pipeline.

    Returns:
        Compiled LangGraph application.
    """
    graph = StateGraph(AgentState)
    graph.add_node("researcher", researcher)
    graph.add_node("writer", writer)
    graph.add_node("reviewer", reviewer)

    graph.add_edge(START, "researcher")
    graph.add_edge("researcher", "writer")
    graph.add_edge("writer", "reviewer")
    graph.add_edge("reviewer", END)

    return graph.compile()
```

---

## C# examples (Semantic Kernel)

### 1. Minimal chat agent

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;

var kernel = Kernel.CreateBuilder()
    .AddOpenAIChatCompletion("gpt-4o", Environment.GetEnvironmentVariable("OPENAI_API_KEY")!)
    .Build();

var chat = kernel.GetRequiredService<IChatCompletionService>();
var history = new ChatHistory("You are a helpful assistant.");

history.AddUserMessage("What is retrieval-augmented generation?");
var response = await chat.GetChatMessageContentAsync(history);
Console.WriteLine(response.Content);
```

### 2. Tool-using agent with plugins

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Agents;
using System.ComponentModel;

public class WeatherPlugin
{
    [KernelFunction, Description("Get the current weather for a city")]
    public string GetWeather(
        [Description("City name")] string city)
    {
        // Replace with actual weather API call
        return $"The weather in {city} is 18°C and partly cloudy.";
    }
}

public class CalculatorPlugin
{
    [KernelFunction, Description("Calculate a mathematical expression")]
    public double Calculate(
        [Description("Mathematical expression")] string expression)
    {
        var table = new System.Data.DataTable();
        return Convert.ToDouble(table.Compute(expression, null));
    }
}

// Build kernel with plugins
var kernel = Kernel.CreateBuilder()
    .AddOpenAIChatCompletion("gpt-4o", apiKey)
    .Build();

kernel.Plugins.AddFromType<WeatherPlugin>();
kernel.Plugins.AddFromType<CalculatorPlugin>();

// Create agent with automatic tool calling
var agent = new ChatCompletionAgent
{
    Kernel = kernel,
    Name = "ToolAgent",
    Instructions = "You are a helpful assistant. Use the available tools to answer questions.",
    Arguments = new KernelArguments(
        new OpenAIPromptExecutionSettings { FunctionChoiceBehavior = FunctionChoiceBehavior.Auto() }
    ),
};

var thread = new ChatHistoryAgentThread();
var response = await agent.InvokeAsync("What is the weather in Amsterdam and what is 42 * 17?", thread);
Console.WriteLine(response.Content);
```

### 3. Swappable providers (Ollama on-premises)

```csharp
using Microsoft.SemanticKernel;

// Configuration-driven provider selection
var backend = Environment.GetEnvironmentVariable("LLM_BACKEND") ?? "ollama";
var model = Environment.GetEnvironmentVariable("LLM_MODEL") ?? "llama3.2";

var builder = Kernel.CreateBuilder();

switch (backend)
{
    case "ollama":
        builder.AddOpenAIChatCompletion(
            modelId: model,
            apiKey: null,
            httpClient: new HttpClient
            {
                BaseAddress = new Uri("http://localhost:11434/v1")
            });
        break;
    case "openai":
        builder.AddOpenAIChatCompletion(
            modelId: model,
            apiKey: Environment.GetEnvironmentVariable("OPENAI_API_KEY")!);
        break;
    case "azure":
        builder.AddAzureOpenAIChatCompletion(
            deploymentName: model,
            endpoint: Environment.GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT")!,
            apiKey: Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY")!);
        break;
    default:
        throw new ArgumentException($"Unknown backend: {backend}");
}

var kernel = builder.Build();
```

### 4. Multi-agent conversation

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Agents;
using Microsoft.SemanticKernel.Agents.Chat;

var kernel = Kernel.CreateBuilder()
    .AddOpenAIChatCompletion("gpt-4o", apiKey)
    .Build();

var researcher = new ChatCompletionAgent
{
    Kernel = kernel,
    Name = "Researcher",
    Instructions = "You research topics and provide factual information with sources.",
};

var critic = new ChatCompletionAgent
{
    Kernel = kernel,
    Name = "Critic",
    Instructions = "You review research for accuracy, bias, and missing perspectives.",
};

var groupChat = new AgentGroupChat(researcher, critic)
{
    ExecutionSettings = new AgentGroupChatSettings
    {
        TerminationStrategy = new MaxTurnTermination(maxTurns: 4),
    },
};

groupChat.AddChatMessage(new ChatMessageContent(
    AuthorRole.User,
    "Analyse the pros and cons of on-premises AI deployment for healthcare."
));

await foreach (var message in groupChat.InvokeAsync())
{
    Console.WriteLine($"[{message.AuthorName}]: {message.Content}");
}
```
