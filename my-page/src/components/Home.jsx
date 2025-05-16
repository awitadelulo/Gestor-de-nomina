import React, { useState } from 'react';
import '../style/Home.css';
import { useNavigate } from 'react-router-dom';

const Home = () => {
  const navigate = useNavigate();
  const [showDropdown, setShowDropdown] = useState(false);

  const toggleDropdown = () => {
    setShowDropdown(prev => !prev);
  };

  return (
    <div className="home-container">
      <h1 className="home-title">Panel Principal</h1>
      <div className="button-group">
        <div className="dropdown">
          <button className="home-button" onClick={toggleDropdown}>
            Administrar Empleado
          </button>
          {showDropdown && (
            <div className="dropdown-menu">
              <button className="dropdown-item" onClick={() => navigate('/AgregarUsuario')}>Agregar</button>
              <button className="dropdown-item" onClick={() => navigate('/ActualizarEmpleado')}>Actualizar</button>
              <button className="dropdown-item" onClick={() => navigate('/EliminarUsuario')}>Eliminar</button>
            </div>
          )}
        </div>

        <button className="home-button" onClick={() => navigate('/MostrarEmpleados')}>Administrar Empleados</button>
        <button className="home-button" onClick={() => navigate('/MostrarProyectosActivos')} >Proyectos Activos</button>
        <button className="home-button" onClick={() => navigate('/VwNomina')} >Detalle Nomina Empleados</button> 
        <button className="home-button">Nomina Empleados</button>
        <button className="home-button">Liquidación Empleados</button>
      </div>
    </div>
  );
};

export default Home;