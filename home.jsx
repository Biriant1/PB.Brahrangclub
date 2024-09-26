import React from 'react';

const Home = () => {
  return (
    <div>
      <h1>Badminton Club</h1>
      <p>Welcome to our badminton club!</p>
      <nav>
        <ul>
          <li><a href="/register">Register</a></li>
          <li><a href="/athletes">Athletes</a></li>
          <li><a href="/events">Events</a></li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;