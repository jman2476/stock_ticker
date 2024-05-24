import { useState, useEffect } from 'react'
import '../App.css'
import axios from 'axios'


function TickerForm() {
  const [tickerSymbol, setTickerSymbol] = useState('AAPL')
  const [tickerText, setTickerText] = useState('')
  const [countyBoy, setCountyBoy] = useState(0)


  const tickerChange = () => {
    setTickerSymbol(tickerText)
  }

  
  
  useEffect(() => {
    const clockInterval = setInterval((x=0) => {
      console.log(tickerSymbol, ' symbol')
      console.log(tickerText, ' text')
      // send post request to the backend using the current ticker symbol
      axios.post('http://localhost:5000/api/symbol', {
        symbol: tickerSymbol
      })
        .then((response) => console.log(response))
        .catch((error) => console.log(error))
    }, 15000);

    return () => clearInterval(clockInterval)

  }, [tickerSymbol])
  // const showSelf = (event) => {
  //   console.log(event.target)
  //   console.log()
  // }

  

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