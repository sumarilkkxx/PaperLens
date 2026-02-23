# PaperLens

<div align="center">

<img src="static/images/github_banner.png" width="100%" />

**An AI-native tool for customizable paper pushes and streamlined reading.**

[English](README.md) | [中文](README_zh.md)

</div>

---


## 📖 Introduction

**PaperLens** is a next-generation research assistant that streamlines the entire academic workflow—from discovery to comprehension to organization. It combines advanced AI with a robust document management system, helping you find, read, understand, and manage papers faster and with less friction.

Whether you’re tracking the latest ArXiv preprints or diving deep into dense PDFs, PaperLens works as your intelligent co-pilot for research.

> **Note**: Most of the frontend code in this project was built with the help of **Cursor**. Honestly, the **Coding Agent** feels a bit magical—it let me ship a usable frontend *way* faster than I ever thought I could. 🤯  
>It’s been a long time since I last wrote frontend code.(the last time was during my undergrad, when I was building mini-programs.)

## ✨ Core Features

<img src="static/images/github_core_future.png" width="100%" />

### 📚 Smart Paper Management
- **Seamless Upload**: Drag & drop PDF uploads with automatic metadata extraction.
- **Organization**: Custom categories, folders, and full-text search.
- **Zotero Integration**: One-click import from Zotero RDF libraries.
- **Reading Heatmap**: Visualize your reading habits with a GitHub-style contribution graph.


### 🤖 AI-Powered Reading Assistant
- **AI Translation**: Generate pixel-perfect English-to-Chinese (and other languages) translations using **BabelDOC**, preserving original layout and charts.
- **AI Interpretation**: Deep analysis of papers using **MinerU** (PDF-to-Markdown) and LLMs to generate structured summaries (Abstract, Methods, Experiments, Conclusions).
- **Chat with Paper**: Interactive Q&A with your documents to clarify concepts and details.

### 📡 Daily ArXiv Radar
- **Automated Tracking**: Schedule daily fetches from specific ArXiv categories (e.g., `cs.CV`, `cs.AI`).
- **Smart Filtering**: Filter papers by keywords, institution weights, and more.
- **AI Summarization**: Automatically generate concise summaries for new arrivals.
- **Offline Capable**: Works even without LLM connections (skips summary/institution details).

## 📸 Feature Showcase

### 📡 Daily ArXiv Tracking
Automated daily paper fetching with AI summaries to keep you updated.
<div align="center">
  <img src="static/images/snapshots/Daily-arxiv-1.png" width="48%" />
  <img src="static/images/snapshots/Daily-arXiv-2.png" width="48%" />
</div>

### 🤖 AI Interpretation & Chat
Deep full-text analysis and interactive Q&A to bridge language and understanding gaps.
<div align="center">
  <img src="static/images/snapshots/AI-Interpretion.png" width="48%" />
  <img src="static/images/snapshots/AI-Chat.png" width="48%" />
</div>

### 📚 Management & Configuration
Efficient reading list management and flexible system configuration.
<div align="center">
  <img src="static/images/snapshots/Reading-List.png" width="48%" />
  <img src="static/images/snapshots/setting-overview.png" width="48%" />
</div>

<div align="center">
  <img src="static/images/snapshots/setting-1.png" width="48%" />
  <img src="static/images/snapshots/setting-daily-arxiv.png" width="48%" />
</div>


## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Flask
- **Frontend**: HTML5, CSS3, Vanilla JS (Responsive)
- **Database**: SQLite (Metadata), Supabase (Optional Auth)
- **AI Core**:
  - [MinerU](https://github.com/opendatalab/MinerU) (High-fidelity PDF parsing)
  - [BabelDOC](https://github.com/funstory-ai/BabelDOC) (Document Translation)
  

## 🚀 Installation

 Recommend using [uv](https://github.com/astral-sh/uv) for fast and reliable dependency management.

### Prerequisites
- Python 3.10 or higher
- `uv` package manager

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/flyflypeng/PaperLens
   cd PaperLens
   ```

2. **Initialize Environment**
   ```bash
   uv venv
   source .venv/bin/activate  # Linux/macOS
   # .venv\Scripts\activate   # Windows
   ```

3. **Install Dependencies**
   
   **Option A: Standard (Client-only)**
   Suitable if you use external APIs for AI tasks.
   ```bash
   uv pip install -e ".[local]"
   ```

   **Option B: Full Server (Local AI)**
   Includes dependencies for local MinerU and VLM inference.
   ```bash
   uv pip install -e ".[server]"
   ```

4. **Supabase Auth (Optional)**
   PaperLens’s login/sign-up is powered by Supabase Auth (Email + Password). When enabled, the frontend uses `supabase-js` in the browser to obtain a session token and attaches `Authorization: Bearer <access_token>` to `/api/*` requests; the backend validates the token via Supabase `/auth/v1/user`.
   If `SUPABASE_URL` and `SUPABASE_ANON_KEY` are not configured, auth is disabled by default: the login overlay is hidden, and `/api/*` endpoints do not require an `Authorization` header, so you can enter the management UI directly.

   1) Create a Supabase project and get API values
   - Create a project at https://supabase.com/
   - In the Supabase dashboard, open **Project Settings → API**
   - Copy **Project URL** as `SUPABASE_URL`
   - Copy **Project API keys → anon public** as `SUPABASE_ANON_KEY`

   2) Enable Email auth
   - Go to **Authentication → Providers**
   - Enable **Email** (Email/Password)
   - For local/private deployments, you can disable email confirmations in **Authentication → Settings** to avoid requiring email verification after sign-up

   3) Configure redirect URLs (important)
   - Go to **Authentication → URL Configuration**
   - Set **Site URL** to your site origin, for example:
   - Local: `http://localhost:7191`
   - Production: `https://your-domain.com`
   - Add allowed callback URLs in **Redirect URLs** (at least include your site root), for example:
   - `http://localhost:7191/`
   - `https://your-domain.com/`

   4) Enable auth in PaperLens
   Copy and edit environment variables in the project root:
   ```bash
   cp .env.example .env
   # Edit .env and fill in SUPABASE_URL and SUPABASE_ANON_KEY
   ```
   Restart the server. If configured correctly, you will see the login/sign-up entry on the page.

   **Security notes**
   - Use only the `anon public` key; never put `service_role` keys into `.env` or ship them to the browser
   - This project injects `SUPABASE_URL` and `SUPABASE_ANON_KEY` into pages for browser-side login, which is expected


5. **Run the Application**

   Then start the application:
   ```bash
   python app.py
   ```
   Access the web interface at `http://localhost:7191` (default port).

   **Custom Launch Arguments:**
   `app.py` supports the following command-line arguments for custom configuration:

   | Argument | Default | Description |
   | :--- | :--- | :--- |
   | `--papers-dir` | `./papers` | Path to the papers directory (absolute or relative) |
   | `--host` | `0.0.0.0` | Server listening address |
   | `--port` | `7191` | Server listening port |
   | `--debug` | `False` | Enable debug mode (for development) |

   **Typical Configuration Examples:**

   - **Specify Data Storage Location** (useful for mounted data volumes):
     ```bash
     python app.py --papers-dir /mnt/data/my_papers
     ```

   - **Change Server Port** (if the default port is occupied):
     ```bash
     python app.py --port 8080
     ```

   - **Allow Local Access Only** (for enhanced security):
     ```bash
     python app.py --host 127.0.0.1
     ```

## ⚙️ Configuration

### Agentic Settings
Navigate to the **Settings** tab to configure:
- **LLM Provider**: Set your API Key, Base URL, and Model Name (e.g., GPT-5.2, Gemini-3-pro, DeepSeek).
- **MinerU**: Choose between Local instance or Cloud API.

### Daily ArXiv
Configure your research interests:
- **Categories**: Select ArXiv categories to monitor.
- **Keywords**: Define keywords for filtering and highlighting.
- **Schedule**: Set the automatic fetch interval.

## ⚠️ Important Notes

- **Multi-User Support**: The current version of PaperLens is designed for individuals or small teams and does not yet fully support multi-tenancy. While it supports authentication via Supabase, all users share the same backend configuration and paper library. It is recommended to deploy in a private network or trusted environment.
- **BabelDOC Translation**: The English-Chinese parallel translation feature based on BabelDOC has high memory consumption and a long processing time. It is recommended to use this feature primarily for papers that require intensive reading.

## 🗺️ Roadmap

### Near-Term (Next)
- [ ] Reading annotations: highlights, comments, bookmarks, and one-click quote snippets
- [ ] Library polish: better search, filters (tags/authors/venues), and smart sorting
- [ ] Import pipeline: faster PDF ingestion, metadata auto-fill, and duplicate detection
- [ ] Reading experience: smoother viewer performance, keyboard shortcuts, and better pagination
- [ ] Deployment & ops: Docker Compose, automated backup/restore, health checks

### Long-Term (Future)
- [ ] Frontend revamp: rebuild the UI with **React** + **shadcn/ui** for a cleaner, more consistent experience
- [ ] RAG & indexing upgrade: hybrid search (BM25 + embeddings), better chunking, and faster retrieval
- [ ] Personal research workspace: projects, reading lists, goals, and progress tracking
- [ ] Export & integration: BibTeX/EndNote/Markdown export, Obsidian/Notion-friendly formats, and API/webhooks
- [ ] Quality & reliability: caching, incremental indexing, observability (logs/metrics/traces), and load testing


## 📄 License

This project is licensed under the **CC BY-NC 4.0** License. See the [LICENSE](LICENSE) file for details.

---

