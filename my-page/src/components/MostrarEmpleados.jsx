import React, { useEffect, useState } from 'react';
import EmployeeCard from './General';
import '../style/General.css';

const MostrarEmpleados = () => {
  const [empleados, setEmpleados] = useState([]);

  // Aquí puedes simular una llamada a una API o usar fetch en producción
  useEffect(() => {
    const empleadosEjemplo = [
      {
        id: 1,
        nombre: "Laura",
        apellidos: "Martínez",
        salarioBasico: 4500000,
        fechaContratacion: "2021-03-15",
        tipoContrato: "Indefinido",
        proyectos: [
          {
            nombreProyecto: "Sistema de Nómina",
            inicioContrato: "2021-03-15",
            finContrato: "2022-06-01",
            fechaInicio: "2021-03-01",
            fechaFin: "2022-12-31",
            estadoProyecto: "Finalizado"
          }
        ]
      },
      {
        id: 2,
        nombre: "Carlos",
        apellidos: "Ruiz",
        salarioBasico: 3800000,
        fechaContratacion: "2020-10-10",
        tipoContrato: "Temporal",
        proyectos: []
      }
    ];
    setEmpleados(empleadosEjemplo);
  }, []);

  return (
    <div className="mostrar-empleados">
      <h1>Lista de Empleados</h1>
      {empleados.map(emp => (
        <EmployeeCard key={emp.id} employee={emp} />
      ))}
    </div>
  );
};

export default MostrarEmpleados;
