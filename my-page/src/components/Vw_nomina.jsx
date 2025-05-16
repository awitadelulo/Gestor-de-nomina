import React, { useState, useEffect } from 'react';
import '../style/VwNomina.css';

const VwNomina = () => {
  const [nominas, setNominas] = useState([]);
  const [nombreFiltro, setNombreFiltro] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchNominas = async (nombre = '') => {
    setLoading(true);
    try {
      let url = 'http://localhost:8000/vw_nomina/';
      if (nombre.trim()) {
        url += encodeURIComponent(nombre.trim());
      }
      const response = await fetch(url);
      if (!response.ok) throw new Error('Error al obtener datos');
      const data = await response.json();
      setNominas(data);
    } catch (error) {
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  // Al cargar por primera vez
  useEffect(() => {
    fetchNominas();
  }, []);

  // Debounce manual para evitar peticiones en cada tecla
  useEffect(() => {
    const delay = setTimeout(() => {
      if (nombreFiltro.length === 0 || nombreFiltro.length > 2) {
        fetchNominas(nombreFiltro);
      }
    }, 300); // 300ms de espera

    return () => clearTimeout(delay);
  }, [nombreFiltro]);

  return (
    <div className="vw-nomina-container">
      <h1>Detalle Nómina</h1>

      <input
        type="text"
        placeholder="Buscar por nombre del empleado..."
        value={nombreFiltro}
        onChange={(e) => setNombreFiltro(e.target.value)}
        className="input-buscar"
      />

      {loading && <div className="loader-text">Buscando...</div>}

      <table className="nomina-table">
        <thead>
          <tr>
            <th>ID Nómina</th>
            <th>ID Empleado</th>
            <th>Empleado</th>
            <th>Concepto</th>
            <th>Valor</th>
          </tr>
        </thead>
        <tbody>
          {nominas.length > 0 ? (
            nominas.map((item) => (
              <tr key={`${item.id_nomina}-${item.id_empleado}-${item.concepto}`}>
                <td>{item.id_nomina}</td>
                <td>{item.id_empleado}</td>
                <td>{item.empleado}</td>
                <td>{item.concepto}</td>
                <td>${item.valor.toFixed(2)}</td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="5">No se encontraron registros.</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
  );
};

export default VwNomina;
