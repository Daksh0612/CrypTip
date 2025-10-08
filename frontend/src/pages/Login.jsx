import React, {useState} from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom'

export default function Login(){
  const [email,setEmail]=useState('admin@cryptip.local')
  const [password,setPassword]=useState('admin123')
  const [err,setErr]=useState('')
  const nav = useNavigate()

  const submit = async (e) => {
    e.preventDefault()
    try{
      const form = new URLSearchParams()
      form.append('username', email)
      form.append('password', password)
      const res = await axios.post(import.meta.env.VITE_API_BASE + '/auth/login', form)
      localStorage.setItem('token', res.data.access_token)
      nav('/dashboard')
    }catch(e){
      setErr(e?.response?.data?.detail || e.message)
    }
  }

  return (
    <div className="card center">
      <h2>Login</h2>
      <form onSubmit={submit}>
        <label>Email</label>
        <input value={email} onChange={e=>setEmail(e.target.value)} />
        <label>Password</label>
        <input type="password" value={password} onChange={e=>setPassword(e.target.value)} />
        <button type="submit">Login</button>
      </form>
      {err && <div className="error">{err}</div>}
      <div className="muted">Use seeded admin (admin@cryptip.local / admin123) after seeding demo</div>
    </div>
  )
}