// NuevoEmpleado.jsx
import React, { useState } from 'react';
import '../style/AgregarUsuario.css';

const ActualizarEmpleado = () => {
  const [form, setForm] = useState({
    nombre: '',
    apellidos: '',
    salario: '',
    tipoContrato: '',
    fechaContratacion: '',
    proyecto: '',
    tipoContratoProyecto: '',
    inicioContrato: '',
    finContrato: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Datos enviados:', form);
    // Aquí puedes hacer la petición POST al backend
  };

  return (
    <div className="form-container">
      <h2>Actualizar Empleado</h2>
      <form onSubmit={handleSubmit}>
        <label>Nombre:</label>
        <input type="text" name="nombre" value={form.nombre} onChange={handleChange} required />

        <label>Apellidos:</label>
        <input type="text" name="apellidos" value={form.apellidos} onChange={handleChange} required />

        <label>Salario Básico:</label>
        <input type="number" name="salario" value={form.salario} onChange={handleChange} required />

        <label>Tipo de Contrato:</label>
        <select name="tipoContrato" value={form.tipoContrato} onChange={handleChange} required>
          <option value="">Seleccione...</option>
          <option value="1">Término fijo</option>
          <option value="2">Indefinido</option>
          <option value="3">Prestación de servicios</option>
        </select>

        <label>Fecha de Contratación:</label>
        <input type="date" name="fechaContratacion" value={form.fechaContratacion} onChange={handleChange} required />

        <h3>Asignación a Proyecto</h3>

        <label>Proyecto:</label>
        <select name="proyecto" value={form.proyecto} onChange={handleChange} required>
          <option value="">Seleccione...</option>
          <option value="1">Proyecto A</option>
          <option value="2">Proyecto B</option>
          <option value="3">Proyecto C</option>
        </select>

        <label>Tipo de Contrato en Proyecto:</label>
        <select name="tipoContratoProyecto" value={form.tipoContratoProyecto} onChange={handleChange} required>
          <option value="">Seleccione...</option>
          <option value="1">Término fijo</option>
          <option value="2">Indefinido</option>
        </select>

        <label>Inicio de Contrato:</label>
        <input type="date" name="inicioContrato" value={form.inicioContrato} onChange={handleChange} required />

        <label>Fin de Contrato:</label>
        <input type="date" name="finContrato" value={form.finContrato} onChange={handleChange} required />

        <button type="submit">Registrar Empleado</button>
      </form>
    </div>
  );
};

export default ActualizarEmpleado;
