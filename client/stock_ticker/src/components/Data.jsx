import { useState, useEffect } from 'react'
import '../App.css'
import '../styles/components/Data.css'
import axios from 'axios'

async function getQuotes(){
    const quotes = fetch()

}

function Data() {
    const [finnQuote, setFinnQuote] = useState('$0')
    const [twelveQuote, setTwelveQuote] = useState('$0')
    const [yFinQuote, setyFinQuote] = useState('$0')
    const [meanQuote, setMeanQuote] = useState('$0')
    const [finnSpread, setFinnSpread] = useState('$0')
    const [twelveSpread, setTwelveSpread] = useState('$0')
    const [yFinSpread, setyFinSpread] = useState('$0')

    useEffect(() => {
        axios.get('http://localhost:5000/api/quotes')
                .then((res) => {
                    setFinnQuote(res.data.finnhub)
                    setTwelveQuote(res.data.twelve_data)
                    setyFinQuote(res.data.yfinance)
                })
        
        const refreshInterval = setInterval(() => {
            axios.get('http://localhost:5000/api/quotes')
                .then((res) => {
                    setFinnQuote(res.data.finnhub)
                    setTwelveQuote(res.data.twelve_data)
                    setyFinQuote(res.data.yfinance)
                })
        }, 15000)

        return () => clearInterval(refreshInterval)
    }, [])

    useEffect(() => {
        axios.get('http://localhost:5000/api/average')
            .then((res) => {
                setMeanQuote(res.data.average)
            })
    }, [])

    useEffect(() => {
        axios.get('http://localhost:5000/api/spread')
            .then((res) => {
                setFinnSpread(res.data.finnhub)
                setTwelveSpread(res.data.twelve_data)
                setyFinSpread(res.data.yfinance)
            })
    }, [])


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