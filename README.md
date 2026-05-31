# UniGraph Student Plotter

A low-barrier plotting app for physics, accounting, and finance students.

## Path 1: Local Desktop App

```powershell
pip install -r requirements.txt
python app.py
```

This is the preferred path for local classroom use and future `.exe` packaging.
All current learning and plotting features are free and do not require login.
The login button opens `https://unigraph.online` for future online account features.

## Package Desktop App as EXE

```powershell
.\build_exe.ps1
```

The generated app will be in `dist\UniGraph.exe`.
This single `.exe` can run on Windows computers without a Python environment.

Notes for distribution:

- Send users `dist\UniGraph.exe`.
- On first launch, the app shows a startup dialog with language selection, login, support/tip, loading text, and `Copyright bowen`.
- The selected language is remembered on the user's computer for later launches.
- The first launch can be slower because the packaged app unpacks its runtime internally.

## Path 2: Web App

```powershell
pip install -r requirements.txt
streamlit run web_app.py
```

Then open the local URL printed by Streamlit, usually `http://localhost:8501`.

## Official Website

The static product website is in `web\`.
It supports English, Chinese, and French with a browser-side language switcher.

Open it locally with:

```powershell
Start-Process .\web\index.html
```

The website download button points to the latest GitHub Release asset:
`https://github.com/bowenCA0/UniGraph/releases/latest/download/UniGraph.exe`.
This keeps large downloads on GitHub instead of the website server.
Replace the Xiaohongshu placeholder link in `web\index.html` with your personal profile URL when ready.
The GitHub open-source link is currently a placeholder and can be filled in later.

## Features

- Chinese, English, and French interface.
- Startup dialog with language selection, loading state, login entry, support/tip button, and `Copyright bowen`.
- Import `.csv`, `.xlsx`, or `.xls` files.
- Select X/Y ranges by row and column for physics-style plotting.
- Choose vertical or horizontal data ranges.
- Scatter, line, bar, histogram, pie, waterfall, finance risk, portfolio, and correlation views.
- Optional axis display, units, error bars, linear fit, polynomial fit, and slope calculation over a chosen point range.
- Image parameter dialog for title, X/Y axis names, units, data color, fit color, grid color, and scientific notation.
- Chart titles plus a compact right-side figure explorer; clicking a plot opens it, New Figure creates the next slot, right-click can delete a plot, and Dual Y-axis opens a checkbox confirmation dialog.
- Resizable and collapsible left/right sidebars.
- One-click experiment analysis with selectable X range and optional chart annotations for regression line, equation, slope, intercept, r, and R².
- Generates a reusable Python script based on the selected settings.

## Development Roadmap

1. Local desktop app: build and test student workflows, then package as `.exe`.
2. Shared analysis core: move file reading, range selection, fitting, slope, and finance/accounting calculations into reusable modules.
3. Web app: reuse the same core with a browser interface for online deployment.
4. Course templates: add sample physics experiments, accounting reports, and finance portfolio cases.
