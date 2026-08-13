import React, { Suspense } from 'react';
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
        {/* Lighting */}
        <ambientLight intensity={0.6} />
        <directionalLight 
          position={[50, 40, 30]} 
          intensity={1.2} 
          castShadow 
        />
        
        {/* Diagnostic Red Test Cube */}
        <mesh position={[0, 1.5, 10]}>
          <boxGeometry args={[0.5, 0.5, 0.5]} />
          <meshStandardMaterial color="#ef4444" />
        </mesh>

        {/* Suspense boundary for Drei async assets (Sky, Troika Text) */}
        <Suspense fallback={null}>
          <Sky 
            distance={450000} 
            sunPosition={[100, 40, 100]} 
            inclination={0.5} 
            azimuth={0.25} 
          />
          <fog attach="fog" args={['#e0ded7', 15, 90]} />
          <Day1World onSelectProvenance={onSelectProvenance} />
        </Suspense>

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
