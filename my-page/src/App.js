import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Login from '../src/components/Login';
import Home from '../src/components/Home';
import AgregarUsuario from '../src/components/AgregarUsuario';
import EliminarUsuario from '../src/components/EliminarUsuario';
import ActualizarEmpleado from '../src/components/ActualizarUsuario';
import MostrarEmpleados from '../src/components/MostrarEmpleados';
function App() {
  return (
  <Router>
      <div>
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/Home" element={<Home/>}/>
          <Route path="/AgregarUsuario" element={<AgregarUsuario/>}/>
          <Route path="/EliminarUsuario" element={<EliminarUsuario/>}/>
          <Route path="/ActualizarEmpleado" element={<ActualizarEmpleado/>}/>
          <Route path="/MostrarEmpleados" element={<MostrarEmpleados />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
