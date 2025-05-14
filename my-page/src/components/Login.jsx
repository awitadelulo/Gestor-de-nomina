import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../style/Login.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault(); // Prevenir recarga

    if (username === 'nomina' && password === '12345') {
      navigate('/Home'); // Redirige a Home si es correcto
    } else {
      alert('Usuario o contraseña incorrectos');
    }
  };

  return (
    <div className="login-background">
      <div className="login-container">
        <h2 className="login-title">Sign In</h2>
        <form className="login-form" onSubmit={handleLogin}>
          <label>Username</label>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />

          <label>Password</label>
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button type="submit" className="login-button">Log In</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
