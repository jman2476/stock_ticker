import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import { TickerForm, Data } from './components'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Stock Ticker</h1>
      
      <TickerForm />
      <Data className='row'/>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
