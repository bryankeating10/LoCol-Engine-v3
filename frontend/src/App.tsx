import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_BASE_URL}/api/health`)
      .then((res) => res.json())
      .then((data) => setMessage(data.status))
      .catch(() => setMessage("Error connecting to backend"));
  }, []);

  return (
    <div>
      <h1>LoCol Engine v3</h1>
      <p>Backend status: {message}</p>
    </div>
  );
}

export default App;