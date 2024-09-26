import React, { useState, useEffect } from 'react';

const AthleteList = () => {
  const [athletes, setAthletes] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('/api/athletes')
      .then(response => response.json())
      .then(data => {
        setAthletes(data);
        setLoading(false);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>Athletes</h1>
      <ul>
        {athletes.map(athlete => (
          <li key={athlete.id}>
            <h2>{athlete.name}</h2>
            <p>{athlete.bio