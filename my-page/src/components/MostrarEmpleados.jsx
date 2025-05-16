import React, { useEffect, useState } from 'react';
import EmployeeCard from './General';
import '../style/General.css';

const MostrarEmpleados = () => {
  const [empleados, setEmpleados] = useState([]);
  const [busqueda, setBusqueda] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchEmpleados = async (nombre = '') => {
    try {
      setLoading(true);
      const url = nombre
        ? `http://localhost:8000/MostrarEmpleados/?nombre=${encodeURIComponent(nombre)}`
        : `http://localhost:8000/MostrarEmpleados/`;

      const response = await fetch(url);
      const data = await response.json();
      setEmpleados(data);
    } catch (error) {
      console.error('Error al obtener empleados:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchEmpleados(); // Cargar todos al inicio
  }, []);

  const handleBuscar = () => {
    fetchEmpleados(busqueda);
  };

  return (
    <div className="mostrar-empleados">
      <h1>Lista de Empleados</h1>

      <div className="busqueda">
        <input
          type="text"
          placeholder="Buscar por nombre..."
          value={busqueda}
          onChange={(e) => setBusqueda(e.target.value)}
        />
        <button onClick={handleBuscar}>Buscar</button>
      </div>

      {loading ? (
        <p>Cargando empleados...</p>
      ) : (
        empleados.map(emp => (
          <EmployeeCard key={emp.id} employee={emp} />
        ))
      )}
    </div>
  );
};

export default MostrarEmpleados;
