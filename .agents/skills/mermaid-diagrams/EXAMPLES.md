# Workspace Diagrams Examples (Tailored Templates)

The following production-ready templates are optimized for developer planning documents, system specifications, and agent-coordinated architectures within this workspace.

All templates follow the GitHub-Safe Dialect Rules in [SKILL.md](SKILL.md) — notably: **no YAML `---` config blocks** (GitHub/VS Code bundled renderers reject them; see REFERENCE.md). Use `%%{init}%%` directives or `classDef` styling instead.

---

## 1. Parallel Task Execution Waves (DAG Flowchart)
*Use for PLAN.md to visualize concurrent agent work, dependency waves, and critical-path sync points.*

```mermaid
flowchart TD
    %% No YAML frontmatter config — unsupported by GitHub/VS Code renderers.
    %% classDef below carries all styling.

    Start([Start Project Wave])
    
    %% Wave 1: Independent Setup (Subgraphs group without nesting logic blocks)
    subgraph W1["Wave 1: Base Foundations"]
        direction LR
        Wave1_Task1["Setup Git Worktrees"]
        Wave1_Task2["Generate Configuration Boilerplate"]
    end
    
    Start --> Wave1_Task1
    Start --> Wave1_Task2
    
    %% Synchronisation gate (Router node patterns prevent label clutter)
    Wave1_Task1 & Wave1_Task2 --> SyncGate1{"Wave 1 Approval Gate"}
    
    %% Wave 2: Concurrent Implementation
    subgraph W2["Wave 2: Worker Agents Deployment"]
        direction TD
        Wave2_Writer["Agent A: Coding Modules"]
        Wave2_Validator["Agent B: Parallel Test Runner"]
    end
    
    SyncGate1 --> Wave2_Writer
    SyncGate1 --> Wave2_Validator
    
    %% Complete/Finish Transition
    Wave2_Writer & Wave2_Validator --> SyncGate2{"Final Integration Gate"}
    SyncGate2 --> End([END - Commit to Main])

    %% Styling and Class Associations
    classDef startEnd fill:#22c55e,stroke:#15803d,stroke-width:2px,color:#fff;
    classDef sync fill:#ef4444,stroke:#b91c1c,stroke-width:2px,color:#fff;
    classDef tasks fill:#3b82f6,stroke:#1d4ed8,stroke-width:2.5px,color:#fff;
    
    class Start,End startEnd;
    class SyncGate1,SyncGate2 sync;
    class Wave1_Task1,Wave1_Task2,Wave2_Writer,Wave2_Validator tasks;
```

---

## 2. Game State-Machine & Session Loop Diagram (`stateDiagram-v2`)
*Use for designing simulation game cycles, player session stages, or server-side loops in Minecraft/Roblox simulators.*

```mermaid
%%{init: {'theme': 'forest'}}%%
stateDiagram-v2
    [*] --> InitializeServer
    InitializeServer --> LoadWorkspaceDB : Success
    LoadWorkspaceDB --> PlayerQueue : DB Connected
    
    state PlayerQueue {
        [*] --> QueueCheck
        QueueCheck --> SpawnPlayer : Slot Available
        QueueCheck --> TimeoutDisconnect : Timeout
    }
    
    state InGameSession {
        [*] --> PlayerActiveLoop
        PlayerActiveLoop --> ApplyTickPhysics : Loop Tick
        ApplyTickPhysics --> PlayerActiveLoop : tickDone
        
        state ActionState {
            [*] --> Idle
            Idle --> Gathering : clickAction
            Gathering --> Idle : inventoryFull
            Idle --> Upgrading : spendCurrency
            Upgrading --> Idle : upgradeFinished
        }
    }
    
    SpawnPlayer --> InGameSession : Spawn Success
    InGameSession --> AutosaveState : PlayerDisconnect / Interval
    AutosaveState --> UnloadPlayerAssets : Save Ok
    UnloadPlayerAssets --> [*]
```

---

## 3. Worktree Branching & Coordination Graph (`gitGraph`)
*Use for tracking branching workflows, multi-agent workspaces, and release pipelines.*

```mermaid
gitGraph
    commit id: "Init main"
    commit id: "Draft plan docs"
    branch dev/wave-1-setup
    checkout dev/wave-1-setup
    commit id: "Bootstrap package files"
    commit id: "Add primary schema spec"
    checkout main
    branch dev/parallel-agent-work
    checkout dev/parallel-agent-work
    commit id: "Launch agent team worktree"
    commit id: "Inject module validations"
    checkout main
    merge dev/wave-1-setup id: "Merge Wave1"
    merge dev/parallel-agent-work id: "Merge Wave2"
    commit id: "Final Release" tag: "v1.2.0"
```

---

## 4. Multi-Agent Intercom Coordination Sequence (`sequenceDiagram`)
*Use for detailing communications, request/response paradigms, or telemetry routing between parallel execution agents.*

```mermaid
sequenceDiagram
    autonumber
    actor Boss as Parent (Supervisor Agent)
    participant WorkerA as Worker Agent A (Writer)
    participant WorkerB as Worker Agent B (Validator)
    participant Workspace as Shared Disk File

    Note over Boss, Workspace: Bootstrapping Multi-Agent Coordination Turn
    Boss->>WorkerA: Dispatch "Write Module Implementation" Task
    activate WorkerA
    WorkerA->>Workspace: Write 'src/module.js'
    WorkerA-->>Boss: Dispatched Response & Complete File Reference
    deactivate WorkerA

    Boss->>WorkerB: Dispatch "Validate & Review File Changes"
    activate WorkerB
    WorkerB->>Workspace: Read 'src/module.js' and Exec Tests
    Workspace-->>WorkerB: Returns test failure diagnostics
    alt Test failures found
        WorkerB-->>Boss: Send Test Failures & Stack Trace
        Boss->>WorkerA: Dispatched "Apply fixes & resolve errors"
    else All tests passed
        WorkerB-->>Boss: Send Pass Confirmation Report
    end
    deactivate WorkerB
    
    Boss->>Boss: Merge workspace files & finalize run
```
