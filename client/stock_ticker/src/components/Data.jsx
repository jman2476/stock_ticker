import { useState } from 'react'
import '../App.css'
import '../styles/components/Data.css'

function Data({className}) {
    const [finnQuote, setFinnQuote] = useState('$0')
    const [twelveQuote, setTwelveQuote] = useState('$0')
    const [yFinQuote, setyFinQuote] = useState('$0')
    const [meanQuote, setMeanQuote] = useState('$0')
    const [finnSpread, setFinnSpread] = useState('$0')
    const [twelveSpread, setTwelveSpread] = useState('$0')
    const [yFinSpread, setyFinSpread] = useState('$0')

    return (
        <div className='row'>
            <div>
                <h2>Quotes</h2>
                <h3>Finnhub: {finnQuote}</h3>
                <h3>Twelve Data: {twelveQuote}</h3>
                <h3>yFinance: {yFinQuote}</h3>
            </div>
            <div>
                <h2>Average</h2>
                <h3>{meanQuote}</h3>
            </div>
            <div>
                <h2>Spread</h2>
                <h3>Finnhub: {finnSpread}</h3>
                <h3>Twelve Data: {twelveSpread}</h3>
                <h3>yFinance: {yFinSpread}</h3> 
            </div>
        </div>    
    )
}

export default Data