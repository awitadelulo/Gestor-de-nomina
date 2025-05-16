import './App.css';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Login from '../src/components/Login';
import Home from '../src/components/Home';
import AgregarUsuario from '../src/components/AgregarUsuario';
import EliminarUsuario from '../src/components/EliminarUsuario';
import ActualizarEmpleado from '../src/components/ActualizarUsuario';
import MostrarEmpleados from '../src/components/MostrarEmpleados';
import MostrarProyectosActivos from '../src/components/Proyectos_activos';
import VwNomina from '../src/components/Vw_nomina';

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
          <Route path="/MostrarProyectosActivos" element={<MostrarProyectosActivos />} />
          <Route path="/VwNomina" element={<VwNomina/>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
