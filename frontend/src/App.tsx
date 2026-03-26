import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [backendStatus, setBackendStatus] = useState<string>('checking...')

  useEffect(() => {
    const apiUrl = import.meta.env.VITE_API_URL || 'http://localhost:8000'
    fetch(`${apiUrl}/health`)
      .then((res) => res.json())
      .then((data) => setBackendStatus(data.status))
      .catch(() => setBackendStatus('offline'))
  }, [])

  return (
    <div className="app">
      <h1>Job Kit Machine</h1>
      <p>Backend: <strong>{backendStatus}</strong></p>
    </div>
  )
}

export default App
