# Modern DevOps Practices: Final Project

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)

This repository contains the final project for the **Modern DevOps Practices** course at **FMI** (2025/2026).

The project demonstrates a complete **automated software delivery pipeline** for a Python web application, following modern **DevOps best practices** and covering multiple phases of the **Software Development Life Cycle (SDLC)**.

## Application Overview

The application is a lightweight **Python Flask web service** that returns a random greeting message to the user.

The application logic is intentionally minimal. This allows the project to focus entirely on **automation, security, and the delivery pipeline**, rather than on code complexity.

## Branching Strategy & Workflow

The project follows a **Structured Gitflow Strategy** with **Branch Protection Rules** to ensure code quality and stability.

### 1. Branch Structure
* **`main` (Production):** The stable branch deployed to the Kubernetes cluster. **Protected:** Direct pushes are blocked; changes require a Pull Request.
* **`dev` (Integration):** The staging branch where new features are combined and tested. **Protected:** CI checks must pass before merging.
* **`feature/**` (Development):** Temporary branches used for developing specific tasks.

### 2. Quality Gates
To ensure stability, we enforce **Protection Rules** on both `dev` and `main` branches:
* **Required Status Checks:** The **CI Pipeline** (`ci-pr.yaml`) must pass successfully (Tests + Security Scans) before merging.
* **Pull Request Flow:** Direct commits are disabled to ensure all code is reviewed.

### 3. Workflow Diagram
The diagram below shows the linear flow of code from development to production.

```mermaid
flowchart TD
    %% Nodes
    Dev[Developer Work]
    Feature[Branch: feature/**]
    
    subgraph Integration [Integration Phase]
        PR_Dev[Pull Request to 'dev']
        CI_Dev[CI Pipeline: ci-pr.yaml]
        Merge_Dev[Merge to 'dev']
    end

    subgraph Production [Production Phase]
        PR_Main[Pull Request to 'main']
        CI_Main[CI Pipeline: ci-pr.yaml]
        Merge_Main[Merge to 'main']
    end
    
    subgraph Deployment [Deployment Phase]
        CD[CD Pipeline: cd.yaml]
        K8s[Kubernetes Cluster]
    end

    %% Connections
    Dev -->|Push Code| Feature
    Feature -.->|Trigger| Lint[Linter: feature-lint.yaml]
    
    Feature --> PR_Dev
    PR_Dev --> CI_Dev
    CI_Dev -->|Pass| Merge_Dev
    CI_Dev -->|Fail| Block1[❌ Block Merge]
    
    Merge_Dev --> PR_Main
    PR_Main --> CI_Main
    CI_Main -->|Pass| Merge_Main
    CI_Main -->|Fail| Block2[❌ Block Merge]
    
    Merge_Main -->|Trigger| CD
    CD -->|Rolling Update| K8s
