import React, { useEffect, useState } from 'react';
import '../style/ProyectosActivos.css';

const ProyectosActivos = () => {
  const [proyectos, setProyectos] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchProyectos = async () => {
      setLoading(true);
      try {
        const response = await fetch('http://localhost:8000/proyectos-activos/');
        const data = await response.json();
        setProyectos(data);
      } catch (error) {
        console.error('Error al obtener proyectos activos:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProyectos();
  }, []);

  return (
    <div className="proyectos-activos-container">
      <h1>Proyectos Activos</h1>
      {loading ? (
        <p>Cargando proyectos...</p>
      ) : proyectos.length > 0 ? (
        <table className="proyectos-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            {proyectos.map(proyecto => (
              <tr key={proyecto.id_proyecto}>
                <td>{proyecto.id_proyecto}</td>
                <td>{proyecto.nombre_proyecto}</td>
                <td>{proyecto.estado}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No hay proyectos activos.</p>
      )}
    </div>
  );
};

export default ProyectosActivos;
