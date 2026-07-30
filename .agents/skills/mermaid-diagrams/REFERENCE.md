# Mermaid Diagram Types Reference

This guide provides condensed syntactic blueprints for core and secondary diagram types supported in VS Code & GitHub.

---

## Flowchart (Core DAG Engine)
```mermaid
flowchart TD
    %% Configuration — YAML frontmatter (Mermaid >= v10.8 only)
    %% GitHub and VS Code ship older renderers that do NOT support this.
    %% Fallback for broad compatibility:
    %%   %%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#2563eb'}}}%%
    %% Or skip config entirely if classDef already handles styling.
    ---
    config:
      theme: base
      themeVariables:
        primaryColor: "#2563eb"
    ---
    
    %% Node Shapes
    A(["Stadium Shape"]) --> B["Rectangle"]
    B --> C{"Decision"}
    C -- "Yes" --> D[/"Parallelogram Input"/]
    C -- "No" --> E(("Circle"))
    
    %% Multi-line and styling
    F["Line 1<br/>Line 2"]
    classDef highlight fill:#f59e0b,stroke:#d97706,stroke-width:2px;
    class A,C highlight
```

---

## Core Diagrams Catalog

### 1. Sequence Diagram (`sequenceDiagram`)
```mermaid
sequenceDiagram
    autonumber
    actor U as User
    participant A as Agent
    participant S as Server
    
    U->>A: Request Task
    activate A
    A->>S: Fetch Metadata (REST)
    S-->>A: JSON Result
    A->>A: Validate Input
    alt is valid
        A-->>U: Success (Payload)
    else is invalid
        A-->>U: Failure Error
    end
    deactivate A
```

### 2. State Diagram (`stateDiagram-v2`)
```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> Active : TriggerAction
    
    state Active {
        [*] --> Processing
        Processing --> Verifying : Checksum
        Verifying --> Processing : Retry
    }
    
    Active --> Completed : Success
    Active --> Failed : Error
    Completed --> [*]
    Failed --> [*]
```

### 3. Gantt Chart (`gantt`)
```mermaid
gantt
    title Development Sprint Map
    dateFormat  YYYY-MM-DD
    section Phase 1
    Requirements Gathering   :active, des1, 2026-07-20, 3d
    Design / Spec Writing    :        des2, after des1, 5d
    section Phase 2
    Implementation          :        imp1, after des2, 10d
```

### 4. Git Graph (`gitGraph`)
```mermaid
gitGraph
    commit id: "Initial commit"
    commit id: "Setup main workspace"
    branch feature/agents
    checkout feature/agents
    commit id: "Add system specs"
    commit id: "Refactor core loop"
    checkout main
    merge feature/agents
    commit id: "Release v1.0.0" tag: "v1.0.0"
```

### 5. Mind Map (`mindmap`)
```mermaid
mindmap
  root((Development))
    Architecture
      Microservices
      Serverless
    Language
      TypeScript
      Rust
    Infrastructure
      Docker
      VPS
```

---

## Lazy Diagram Reference (Secondary Types)

### Class Diagram (`classDiagram`)
```mermaid
classDiagram
    direction RL
    class Player {
        +String username
        +int level
        +saveData()
    }
    class Skill {
        +String name
        +activate()
    }
    Player "1" --> "*" Skill : owns
```

### Entity-Relationship Diagram (`erDiagram`)
```mermaid
erDiagram
    PLAYER ||--o{ INVENTORY : has
    PLAYER {
        string userId PK
        string username
        int level
    }
    INVENTORY {
        string itemId PK
        string userId FK
        int quantity
    }
```

### Timeline (`timeline`)
```mermaid
timeline
    title Project Milestones
    2026 Q1 : Kickoff : Core Planning
    2026 Q2 : Prototyping : Agent Core
    2026 Q3 : Release : Scale Deployment
```

### User Journey Map (`journey`)
```mermaid
journey
    title Sign-in Experience
    section Landing
      Access site: 5: Customer
      Check features: 3: Customer
    section Authentication
      Fill username: 4: Customer, Agent
      Perform MFA: 2: Customer
```

### Quadrant Chart (`quadrantChart`)
```mermaid
quadrantChart
    title Feature Priority Map
    x-axis Low Effort --> High Effort
    y-axis Low Value --> High Value
    quadrant-1 High Value, High Effort (Plan)
    quadrant-2 High Value, Low Effort (Execute First)
    quadrant-3 Low Value, Low Effort (De-prioritise)
    quadrant-4 Low Value, High Effort (Avoid)
    "Visualiser" : [0.3, 0.8]
    "Local CI Tooling" : [0.8, 0.4]
```

### Architecture & Block Diagrams (`architecture` / `block-beta`)
```mermaid
block-beta
    columns 3
    FrontendBlock["Frontend UI"] Space FrontendDb[("Local DB")]
    block:middleGroup:3
        columns 2
        API["Backend API"]
        Cache[("Redis")]
    end
    DB[(Global Postgres)]
    FrontendBlock --> API
    API --> Cache
    API --> DB
```

### Other Standard Syntax (Quick Starters)
- **Pie Chart:** `pie title Ratio\n"Used": 75\n"Free": 25`
- **Sankey:** `sankey-beta\nSource,Target,Value\n"A","B",10`
- **XYChart:** `xychart-beta\ntitle "Speed vs Size"\nx-axis [1, 2, 3]\ny-axis "Time" [10, 20, 30]`
- **Radar:** `radar\ntitle "Capability Matrix"\nlabels [Speed, Price, Memory]\nplot1 [10, 20, 30]`
- **Treemap:** `treemap\ntitle "Disk Space"\n"Log": 200\n"Temp": 50`
- **Packet:** `packet-beta\n0-7: "Type"\n8-15: "Length"`
