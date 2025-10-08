import React from 'react'
import { Outlet } from 'react-router-dom'

export default function App(){
  return (
    <div className="app-root">
      <header className="topbar"><h1>Cryptip</h1></header>
      <main className="content"><Outlet/></main>
    </div>
  )
}