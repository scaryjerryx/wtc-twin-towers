import React, { useEffect } from 'react';
import { useTexture } from '@react-three/drei';
import * as THREE from 'three';

export const PathTube: React.FC = () => {
  // Dual parallel PATH tubes spanning diagonally
  const tubeLength = 65; 
  const radius = 2.5; // ~16.4 ft diameter per tube
  const tubeSpacing = 6.0; // Distance between the two parallel tubes
  
  // Angle for diagonal crossing
  const rotationY = Math.PI / 4; 

  const metalMaps = useTexture({
    map: '/textures/metal/Metal035_1K-JPG_Color.jpg',
    metalnessMap: '/textures/metal/Metal035_1K-JPG_Metalness.jpg',
    normalMap: '/textures/metal/Metal035_1K-JPG_NormalGL.jpg',
    roughnessMap: '/textures/metal/Metal035_1K-JPG_Roughness.jpg',
  });

  useEffect(() => {
    Object.values(metalMaps).forEach((texture) => {
      texture.wrapS = THREE.RepeatWrapping;
      texture.wrapT = THREE.RepeatWrapping;
      texture.repeat.set(10, 2);
    });
  }, [metalMaps]);

  return (
    <group position={[-15, -2, -15]} rotation={[0, rotationY, 0]}>
      {/* 1. DUAL Cast Iron Tubes */}
      {[-tubeSpacing / 2, tubeSpacing / 2].map((zOffset, tIndex) => (
        <group key={`tube-${tIndex}`} position={[0, 0, zOffset]}>
          <mesh castShadow receiveShadow rotation={[0, 0, Math.PI / 2]}>
            <cylinderGeometry args={[radius, radius, tubeLength, 32]} />
            <meshStandardMaterial {...metalMaps} color="#a1a1aa" />
          </mesh>

          {/* Cast Iron Segment Flanges (Ribbing every 1.5 meters) */}
          {Array.from({ length: Math.floor(tubeLength / 1.5) }).map((_, i) => {
            const xPos = (-tubeLength / 2) + i * 1.5;
            return (
              <mesh key={`flange-${i}`} position={[xPos, 0, 0]} rotation={[0, 0, Math.PI / 2]} castShadow>
                <cylinderGeometry args={[radius + 0.25, radius + 0.25, 0.15, 32]} />
                <meshStandardMaterial {...metalMaps} color="#292524" />
              </mesh>
            );
          })}
        </group>
      ))}

      {/* 2. Heavy Steel Support Trusses (Every 15 meters) */}
      {[-22, -7, 8, 23].map((xOffset, i) => (
        <group key={`support-${i}`} position={[xOffset, -4, 0]}>
          {/* Massive Shared Cradle underneath both tubes */}
          <mesh position={[0, 1.5, 0]} castShadow>
            <boxGeometry args={[2.5, 1.2, tubeSpacing + 6]} />
            <meshStandardMaterial {...metalMaps} color="#3f3f46" />
          </mesh>
          
          {/* Dual Vertical Columns per cradle */}
          <mesh position={[0, -2.5, tubeSpacing / 2 + 1.5]} castShadow>
            <boxGeometry args={[1.5, 9, 1.5]} />
            <meshStandardMaterial {...metalMaps} color="#27272a" />
          </mesh>
          <mesh position={[0, -2.5, -(tubeSpacing / 2 + 1.5)]} castShadow>
            <boxGeometry args={[1.5, 9, 1.5]} />
            <meshStandardMaterial {...metalMaps} color="#27272a" />
          </mesh>

          {/* Heavy X-Bracing between the columns */}
          <mesh position={[0, -2.5, 0]} rotation={[Math.PI / 3.5, 0, 0]} castShadow>
            <boxGeometry args={[0.8, 10, 0.8]} />
            <meshStandardMaterial {...metalMaps} color="#3f3f46" />
          </mesh>
          <mesh position={[0, -2.5, 0]} rotation={[-Math.PI / 3.5, 0, 0]} castShadow>
            <boxGeometry args={[0.8, 10, 0.8]} />
            <meshStandardMaterial {...metalMaps} color="#3f3f46" />
          </mesh>

          {/* Concrete Footing on the Pit Floor (Y = -8 relative to group center) */}
          <mesh position={[0, -7.5, 0]} castShadow>
            <boxGeometry args={[4.5, 1.5, tubeSpacing + 8]} />
            <meshStandardMaterial color="#52525b" roughness={0.9} />
          </mesh>

          {/* High-visibility safety markings at the base of the columns */}
          <group position={[0, -6.5, tubeSpacing / 2 + 1.5]}>
            <mesh castShadow><boxGeometry args={[1.6, 0.5, 1.6]} /><meshStandardMaterial color="#ea580c" /></mesh>
            <mesh position={[0, 0.5, 0]} castShadow><boxGeometry args={[1.6, 0.5, 1.6]} /><meshStandardMaterial color="#f8fafc" /></mesh>
          </group>
          <group position={[0, -6.5, -(tubeSpacing / 2 + 1.5)]}>
            <mesh castShadow><boxGeometry args={[1.6, 0.5, 1.6]} /><meshStandardMaterial color="#ea580c" /></mesh>
            <mesh position={[0, 0.5, 0]} castShadow><boxGeometry args={[1.6, 0.5, 1.6]} /><meshStandardMaterial color="#f8fafc" /></mesh>
          </group>
        </group>
      ))}
    </group>
  );
};
