import React from 'react';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Sky } from '@react-three/drei';
import { Day1World } from './Day1World';
import { ProvenanceData } from '../ui/ProvenanceModal';

interface ExperienceCanvasProps {
  onSelectProvenance: (data: ProvenanceData) => void;
}

export const ExperienceCanvas: React.FC<ExperienceCanvasProps> = ({ onSelectProvenance }) => {
  return (
    <div className="canvas-container">
      <Canvas
        camera={{ position: [0, 2.5, 14], fov: 60 }}
        shadows
        onCreated={({ gl }) => {
          gl.setClearColor('#e0ded7');
        }}
      >
        {/* 1. Atmospheric Sky & Lighting */}
        <Sky 
          distance={450000} 
          sunPosition={[100, 40, 100]} 
          inclination={0.5} 
          azimuth={0.25} 
        />
        <ambientLight intensity={0.5} />
        <directionalLight 
          position={[50, 40, 30]} 
          intensity={1.2} 
          castShadow 
          shadow-mapSize-width={2048} 
          shadow-mapSize-height={2048} 
        />
        
        {/* 2. Atmospheric Fog (1966 NYC Haze) */}
        <fog attach="fog" args={['#e0ded7', 15, 90]} />

        {/* 3. Day 1 1966 World Scene */}
        <Day1World onSelectProvenance={onSelectProvenance} />

        {/* 4. Controls (Smooth Navigation) */}
        <OrbitControls 
          target={[0, 1, 0]} 
          maxPolarAngle={Math.PI / 2 - 0.05} 
          minDistance={2} 
          maxDistance={60} 
        />
      </Canvas>
    </div>
  );
};
