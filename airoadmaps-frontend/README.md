
# AI Roadmaps Frontend

The frontend of the **AI Roadmaps** project, built with **Next.js** (App Router) and **Tailwind CSS**.

---

## Features

- **User Authentication**:
  - Google login for easy authentication
- **Roadmap Management**:
  - Create and manage personalized learning roadmaps
  - View and delete existing roadmaps
- **Chat with Agent**:
  - Engage in chat with an AI agent to create custom learning roadmaps
- **Responsive Design**:
  - Mobile-first, ensuring a seamless experience across all devices
- **User-Friendly Interface**:
  - UI with smooth interactions for managing and creating roadmaps

---

## Prerequisites

Before getting started, make sure the following are installed:

- **Node.js**: `>= 16.x`
- **npm** or **yarn**: Package manager for managing dependencies

---

## How to setup


1. Install dependencies:

   ```bash
   npm install
   ```

   Or, using yarn:

   ```bash
   yarn install
   ```

2. Configure environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables:
     ```env
     GOOGLE_CLIENT_ID=your_google_client_id  # Google OAuth client ID
     ```

---

## Usage

### Running the development server

Start the development server with:

```bash
npm run dev
```

Or, with yarn:

```bash
yarn dev
```

The app will run on [http://localhost:3000](http://localhost:3000) by default.

---

## Project Structure

### **`/src/`**: Main directory containing all application code

- **`/src/app/`**: Contains the App Router and Next.js page routes
  

- **`/src/components/`**: Reusable UI components
  

- **`/src/context/`**: Global state management using React Context API
  

- **`/src/hoc/`**: Higher-Order Components (HOCs) for common functionality
  

- **`/src/utils/`**: Utility functions. 
**Example:** API helpers
  

---

## Styling

- **Tailwind CSS** is used for responsive design and utility-first styling. 
  - The app is optimized for mobile-first, ensuring a smooth experience across all devices.
---

## Technologies Used

- **Frontend Framework**: Next.js (App Router)
- **Styling**: Tailwind CSS
- **State Management**: React Context API for global state
- **API Communication**: Fetch API for interacting with the backend
- **Authentication**: Google OAuth for user login
---


#