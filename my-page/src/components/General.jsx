import React from "react";
import '../style/General.css';

const EmployeeCard = ({ employee }) => {
  return (
    <div className="employee-card">
      <h2>{employee.nombre} {employee.apellidos}</h2>

      <table className="employee-table">
        <tbody>
          <tr>
            <th>ID</th>
            <td>{employee.id}</td>
          </tr>
          <tr>
            <th>Salario Básico</th>
            <td>${employee.salariobasico.toFixed(2)}</td>
          </tr>
          <tr>
            <th>Fecha de Contratación</th>
            <td>{employee.fechacontratacion}</td>
          </tr>
          <tr>
            <th>Tipo de Contrato</th>
            <td>{employee.tipocontrato}</td>
          </tr>
        </tbody>
      </table>

      <div className="project-section">
        <h3>Proyectos</h3>
        {employee.proyectos.length > 0 ? (
          <table className="project-table">
            <thead>
              <tr>
                <th>Nombre</th>
                <th>Inicio Contrato</th>
                <th>Fin Contrato</th>
                <th>Inicio Proyecto</th>
                <th>Fin Proyecto</th>
                <th>Estado</th>
              </tr>
            </thead>
            <tbody>
              {employee.proyectos.map((proyecto, idx) => (
                <tr key={idx}>
                  <td>{proyecto.nombreproyecto}</td>
                  <td>{proyecto.iniciocontrato}</td>
                  <td>{proyecto.fincontrato}</td>
                  <td>{proyecto.fechainicio}</td>
                  <td>{proyecto.fechafin}</td>
                  <td>{proyecto.estadoproyecto}</td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p>Este empleado no ha participado en proyectos.</p>
        )}
      </div>
    </div>
  );
};

export default EmployeeCard;
