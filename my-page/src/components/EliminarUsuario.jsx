import React, { useState } from "react";
import "../style/EliminarUsuario.css";

export default function EliminarEmpleadoForm() {
  const [nombre, setNombre] = useState("");
  const [apellidos, setApellidos] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Empleado a eliminar:", { nombre, apellidos });
    alert(`Empleado ${nombre} ${apellidos} eliminado.`);
    setNombre("");
    setApellidos("");
  };

  return (
    <div className="form-container">
      <h2 className="form-title">Eliminar Empleado</h2>
      <form onSubmit={handleSubmit} className="form">
        <div className="form-group">
          <label>Nombre</label>
          <input
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
            required
          />
        </div>
        <div className="form-group">
          <label>Apellidos</label>
          <input
            type="text"
            value={apellidos}
            onChange={(e) => setApellidos(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="delete-button">
          Eliminar Empleado
        </button>
      </form>
    </div>
  );
}
