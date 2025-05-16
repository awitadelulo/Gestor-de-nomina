import React, { useState } from "react";
import "../style/EliminarUsuario.css";

export default function EliminarEmpleadoForm() {
  const [nombre, setNombre] = useState("");
  const [apellidos, setApellidos] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:8000/Eliminar/eliminar", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ nombre, apellidos }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Error al eliminar empleado");
      }

      const result = await response.json();
      alert(result.mensaje);
      setNombre("");
      setApellidos("");
    } catch (error) {
      alert("Error: " + error.message);
      console.error("Error:", error);
    }
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
