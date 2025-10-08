import React, {useEffect, useState} from 'react'
import axios from 'axios'

const API = import.meta.env.VITE_API_BASE || 'http://localhost:8000'

export default function Dashboard(){
  const [list,setList]=useState([])
  const [addr,setAddr]=useState('')
  const [chain,setChain]=useState('ETH')
  const [msg,setMsg]=useState('')

  const token = localStorage.getItem('token') || ''

  const fetch = async ()=>{
    try{
      const res = await axios.get(API + '/addresses/list', { headers: { Authorization: 'Bearer '+token }})
      setList(res.data)
    }catch(e){
      console.error(e); setMsg('Failed to fetch addresses: ' + (e?.response?.data?.detail || e.message))
    }
  }

  useEffect(()=>{ fetch() }, [])

  const add = async ()=>{
    try{
      const res = await axios.post(API + '/addresses/add', { address: addr, chain }, { headers: { Authorization: 'Bearer '+token }})
      setMsg('Added: '+res.data.address)
      setAddr(''); fetch()
    }catch(e){
      setMsg('Add failed: ' + (e?.response?.data?.detail || e.message))
    }
  }

  const seed = async ()=>{
    try{
      await axios.post(API + '/sample/seed_demo')
      setMsg('Seeded demo data')
      fetch()
    }catch(e){ setMsg('Seed failed: '+e.message) }
  }

  return (
    <div>
      <div className="grid">
        <div className="card">
          <h3>Quick Actions</h3>
          <div><button onClick={seed}>Seed Demo Data</button></div>
        </div>
        <div className="card">
          <h3>Add Address</h3>
          <input placeholder="0x..." value={addr} onChange={e=>setAddr(e.target.value)} />
          <select value={chain} onChange={e=>setChain(e.target.value)}>
            <option>ETH</option>
            <option>BTC</option>
          </select>
          <button onClick={add}>Add</button>
          <div className="muted">{msg}</div>
        </div>
      </div>

      <div className="card">
        <h3>Address List</h3>
        <table className="table">
          <thead><tr><th>ID</th><th>Address</th><th>Chain</th><th>Category</th><th>Risk</th></tr></thead>
          <tbody>
            {list.map(x=>(
              <tr key={x.id}><td>{x.id}</td><td><code>{x.address}</code></td><td>{x.chain}</td><td>{x.category}</td><td>{x.risk_score}</td></tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}