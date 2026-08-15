import React from 'react';
import { Canvas } from '@react-three/fiber';
import { Sparkles } from '@react-three/drei';
import * as THREE from 'three';
import { Day1World } from './Day1World';
import { FirstPersonControls } from '../controls/FirstPersonControls';
import { ProvenanceData } from '../ui/ProvenanceModal';
import { SiteAudio } from '../audio/SiteAudio';

interface ExperienceCanvasProps {
  onSelectProvenance: (data: ProvenanceData) => void;
  isModalOpen: boolean;
  onHoverTargetChange?: (targetName: string | null) => void;
}

export const ExperienceCanvas: React.FC<ExperienceCanvasProps> = ({
  onSelectProvenance,
  isModalOpen,
  onHoverTargetChange
}) => {
  // Hazy 1966 construction site atmosphere colors
  const skyColor = '#b5ad9e';
  
  return (
    <div className="canvas-container">
      <Canvas
        camera={{ position: [0, 1.7, 10], fov: 80, near: 0.1, far: 500 }}
        shadows
        gl={{ preserveDrawingBuffer: true, antialias: true, toneMapping: THREE.ACESFilmicToneMapping }}
        onCreated={({ gl, scene }) => {
          gl.setClearColor(skyColor);
          scene.background = new THREE.Color(skyColor);
        }}
      >
        {/* Sky Background Color */}
        <color attach="background" args={[skyColor]} />

        {/* Environmental Daylight Lighting: High Contrast for deep shadows */}
        <ambientLight intensity={0.15} />
        <hemisphereLight 
          color="#ffffff" 
          groundColor="#0f0a05" 
          intensity={0.15} 
        />
        <directionalLight 
          position={[30, 45, 20]} 
          intensity={4.5}
          color="#fffaee"
          castShadow 
          shadow-mapSize-width={4096}
          shadow-mapSize-height={4096}
          shadow-bias={-0.0002}
          shadow-camera-left={-50}
          shadow-camera-right={50}
          shadow-camera-top={50}
          shadow-camera-bottom={-50}
          shadow-camera-far={150}
        />
        
        {/* Atmospheric Excavation Fog (Dense Haze) */}
        <fog attach="fog" args={[skyColor, 15, 120]} />

        {/* Airborne Dust Particles */}
        <Sparkles count={3000} scale={150} size={1.5} speed={0.2} opacity={0.15} color="#d4c5b0" noise={1} />

        {/* Procedural Ambient Audio (Traffic, Rumble) */}
        <SiteAudio />

        {/* Day 1 Reconstructed 3D Scene */}
        <Day1World onSelectProvenance={onSelectProvenance} />
        
        {/* First-Person Controller: WASD + Mouse PointerLock + Collision */}
        <FirstPersonControls 
          onSelectProvenance={onSelectProvenance}
          isModalOpen={isModalOpen}
          onHoverTargetChange={onHoverTargetChange}
        />
      </Canvas>
    </div>
  );
};
