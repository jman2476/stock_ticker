import { useState } from 'react'
import '../App.css'

function TickerForm() {
  const [tickerSymbol, setTickerSymbol] = useState('AAPL')
  const [tickerText, setTickerText] = useState('')


  const tickerChange = () => {
    setTickerSymbol(tickerText)
  }

  const showSelf = (event) => {
    console.log(event.target)
    console.log()
  }
  return (
    <>
        <label>Ticker Symbol: </label>
        <input 
            type="text"
            required
            value={tickerText}
            onChange={(event) => setTickerText(event.target.value)} />
        <button onClick={tickerChange}>Get that data</button>

        <p>{tickerSymbol}</p>
        <p>{tickerText}</p>
    </>
  )
}

export default TickerForm