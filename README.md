# CPE0049L: Software Design Laboratory
**Laboratory 1: Cloud-Native Engineering Environment Provisioning**

**Objective:** Establish a standardized, reproducible cloud development environment. Students will utilize GitHub Codespaces to provision an ephemeral Linux container, configure version control, and isolate project dependencies entirely within a web browser, bypassing local hardware and administrative constraints.

### 🛑 CRITICAL PREREQUISITE
**Before clicking any links below, you MUST log into your GitHub account in this web browser.** If you are not logged in, the template link will return a "404 Not Found" error.
* **Requirements:** Any modern web browser (Edge, Chrome, Firefox) and an active GitHub account (registration using the institutional `.edu.ph` email is required to access GitHub Global Campus benefits).
* *No local software installation is required.*

---

### Step 1: Duplicate the Master Workspace
1. Navigate directly to the template generator provided by your instructor:
   **https://github.com/wolverine197535/CPE0049-LAB01-TEMPLATE/generate**
2. In the "Repository name" box, type your assigned format: `CPE0049L_LastName_FirstName` (e.g., `CPE0049L_DelaCruz_Juan`).
3. Set the visibility to **Private**.
4. Click the green **Create repository** button at the bottom.

### Step 2: Launch Your Cloud Terminal
1. In your newly created repository, click the green **<> Code** button.
2. Click the **Codespaces** tab in the dropdown menu.
3. Click the green button **Create codespace on main**.
4. *Wait 1-2 minutes.* A web-based Visual Studio Code interface will load, providing direct access to an Ubuntu container terminal.

### Step 3: Configure Your Engineering Identity
You must link your academic identity to this environment so your work is properly attributed for grading.
1. Open the terminal at the bottom of the screen (or press `` Ctrl + ` ``).
2. Type the following commands exactly, pressing **Enter** after each line. Replace the placeholder text with your actual details:
   ```bash
   git config --global user.name "Your Full Name"
   git config --global user.email "your.email@institution.edu.ph"
   ```
3. Verify it worked by typing:
   ```bash
   git config --list
   ```

### Step 4: Isolate Dependencies and Save State
We will create a Python "Virtual Environment" to keep our workspace organized, and then push our configuration to the cloud so it is permanently saved.
1. In the terminal, execute the following commands:
   ```bash
   # Create the virtual environment folder named '.venv'
   python3 -m venv .venv
   
   # Activate the environment
   source .venv/bin/activate
   
   # Create a file to hide the virtual environment from version control
   echo ".venv/" > .gitignore
   echo "__pycache__/" >> .gitignore
   ```
2. Because cloud containers spin down when inactive, you must push your local commits back to your GitHub repository to save your work:
   ```bash
   # Stage and commit the scaffolding
   git add .gitignore
   git commit -m "chore: initial project scaffolding and gitignore"
   
   # Push the commit to the main branch
   git push origin main
   ```

### Step 5: Generate and Submit Your Telemetry
You must export a log of your terminal commands to prove you completed the laboratory successfully.
1. Execute these final commands:
   ```bash
   # Export your command history to a text file
   history > lab01_history.txt
   
   # Append your current repository status to the same file
   git status >> lab01_history.txt
   ```
2. Look at the file explorer panel on the left side of your screen. You will see a new file named `lab01_history.txt`.
3. Right-click `lab01_history.txt` and select **Download**.
4. Upload this downloaded file to the Week 1 assignment bin in your LMS before the end of the session.
5. Close your browser tab. Your cloud container will automatically spin down and save its state.
