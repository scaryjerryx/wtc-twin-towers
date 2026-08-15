import React, { useEffect } from 'react';
import { useTexture } from '@react-three/drei';
import * as THREE from 'three';

export const VisualStorytelling: React.FC = () => {
  const concreteMaps = useTexture({
    map: '/textures/concrete/Concrete015_2K-JPG_Color.jpg',
    normalMap: '/textures/concrete/Concrete015_2K-JPG_NormalGL.jpg',
    roughnessMap: '/textures/concrete/Concrete015_2K-JPG_Roughness.jpg',
  });

  const metalMaps = useTexture({
    map: '/textures/metal/Metal035_1K-JPG_Color.jpg',
    metalnessMap: '/textures/metal/Metal035_1K-JPG_Metalness.jpg',
    normalMap: '/textures/metal/Metal035_1K-JPG_NormalGL.jpg',
    roughnessMap: '/textures/metal/Metal035_1K-JPG_Roughness.jpg',
  });

  useEffect(() => {
    Object.values(concreteMaps).forEach((texture) => {
      texture.wrapS = THREE.RepeatWrapping;
      texture.wrapT = THREE.RepeatWrapping;
      texture.repeat.set(2, 2);
    });
    Object.values(metalMaps).forEach((texture) => {
      texture.wrapS = THREE.RepeatWrapping;
      texture.wrapT = THREE.RepeatWrapping;
      texture.repeat.set(2, 2);
    });
  }, [concreteMaps, metalMaps]);

  return (
    <group>
      {/* 1. RADIO ROW STOREFRONTS (Forms horizon line in background) */}
      <group position={[15, 0, -25]}>
        {Array.from({ length: 8 }).map((_, i) => {
          const height = 10 + Math.random() * 8;
          const width = 5 + Math.random() * 3;
          const depth = 5;
          const x = -15 + i * (width + 0.5);
          const color = ['#7c2d12', '#854d0e', '#451a03', '#9a3412', '#52525b', '#3f3f46'][i % 6];
          const floors = Math.floor((height - 4) / 3);

          return (
            <group key={`bldg-${i}`} position={[x, 0, 0]} rotation={[0, -0.6, 0]}>
              <mesh position={[0, height / 2, 0]} castShadow receiveShadow>
                <boxGeometry args={[width, height, depth]} />
                <meshStandardMaterial {...concreteMaps} color={color} roughness={0.9} />
              </mesh>
              <mesh position={[0, height + 0.2, 0.2]} castShadow>
                <boxGeometry args={[width + 0.4, 0.6, depth + 0.4]} />
                <meshStandardMaterial {...concreteMaps} color="#27272a" />
              </mesh>
              <mesh position={[0, height - 0.2, 2.6]} castShadow>
                <boxGeometry args={[width + 0.2, 0.4, 0.4]} />
                <meshStandardMaterial color="#18181b" />
              </mesh>
              
              {/* Ground Floor Storefront */}
              <group position={[0, 2, 2.5]}>
                {/* Awning/Signboard */}
                <mesh position={[0, 1.5, 0.2]} castShadow>
                  <boxGeometry args={[width, 1, 0.5]} />
                  <meshStandardMaterial color={['#0f172a', '#1e3a8a', '#7f1d1d'][i % 3]} />
                </mesh>
                {/* Recessed Entrance & Glass */}
                <group position={[0, -0.5, 0]}>
                  {/* Glass Panels */}
                  <mesh position={[0, 0, 0]}>
                    <planeGeometry args={[width * 0.9, 3]} />
                    <meshStandardMaterial color="#020617" roughness={0.1} metalness={0.8} />
                  </mesh>
                  {/* Framing */}
                  <mesh position={[0, 0, 0.05]}>
                    <boxGeometry args={[width * 0.9, 3, 0.1]} />
                    <meshStandardMaterial color="#3f3f46" wireframe />
                  </mesh>
                  {/* Recessed Door */}
                  <mesh position={[0, -0.5, -0.5]}>
                    <boxGeometry args={[1.2, 2, 1]} />
                    <meshStandardMaterial color="#020617" />
                  </mesh>
                </group>
              </group>

              {/* Upper Windows */}
              {Array.from({ length: floors }).map((_, f) => (
                <group key={`floor-${f}`} position={[0, 6 + f * 3, 2.5]}>
                  <mesh position={[-width/4, 0, 0.05]}>
                    <boxGeometry args={[1, 1.6, 0.1]} />
                    <meshStandardMaterial color="#020617" roughness={0.2} metalness={0.6} />
                  </mesh>
                  <mesh position={[width/4, 0, 0.05]}>
                    <boxGeometry args={[1, 1.6, 0.1]} />
                    <meshStandardMaterial color="#020617" roughness={0.2} metalness={0.6} />
                  </mesh>
                </group>
              ))}

              {/* Fire Escape (Ironwork) */}
              {i % 2 === 0 && (
                <group position={[0, height / 2, 2.8]}>
                  <mesh castShadow>
                    <boxGeometry args={[width * 0.8, height - 4, 0.6]} />
                    <meshStandardMaterial color="#18181b" wireframe />
                  </mesh>
                </group>
              )}
            </group>
          );
        })}
      </group>

      {/* 2. CONSTRUCTION EQUIPMENT (High Fidelity Silhouettes) */}
      
      {/* Heavy Crawler Crane */}
      <group position={[7.5, 0, -2]} rotation={[0, 0.5, 0]}>
        {/* Track Assembly (More detailed) */}
        <group position={[0, 0.6, 0]}>
          <mesh position={[-1.8, 0, 0]} castShadow>
            <boxGeometry args={[0.8, 1.2, 6]} />
            <meshStandardMaterial color="#1c1917" roughness={0.9} />
          </mesh>
          <mesh position={[1.8, 0, 0]} castShadow>
            <boxGeometry args={[0.8, 1.2, 6]} />
            <meshStandardMaterial color="#1c1917" roughness={0.9} />
          </mesh>
          {/* Chassis */}
          <mesh castShadow rotation={[Math.PI/2, 0, 0]}>
            <cylinderGeometry args={[1.5, 1.5, 1, 16]} />
            <meshStandardMaterial color="#27272a" />
          </mesh>
        </group>
        {/* Revolving Cab */}
        <group position={[0, 2.5, 0]}>
          <mesh castShadow>
            <boxGeometry args={[3.5, 2.5, 5]} />
            <meshStandardMaterial color="#ea580c" roughness={0.7} />
          </mesh>
          {/* Counterweight */}
          <mesh position={[0, 0, -2.5]} castShadow>
            <boxGeometry args={[3.5, 2.5, 1]} />
            <meshStandardMaterial color="#27272a" />
          </mesh>
          {/* Operator Window */}
          <mesh position={[1.2, 0.2, 2.5]} castShadow>
            <boxGeometry args={[1, 1.5, 0.5]} />
            <meshStandardMaterial color="#020617" />
          </mesh>
          {/* Exhaust Stack */}
          <mesh position={[-1, 1.5, -1]} castShadow>
            <cylinderGeometry args={[0.1, 0.1, 1]} />
            <meshStandardMaterial color="#18181b" />
          </mesh>
        </group>
        {/* Lattice Boom */}
        <group position={[0, 3, 2.5]} rotation={[0.7, 0, 0]}>
          <mesh position={[0, 0, 18]} castShadow>
            <boxGeometry args={[1.2, 1.2, 36]} />
            <meshStandardMaterial color="#ea580c" wireframe />
          </mesh>
          {/* Cables and Icanda Clamshell Bucket */}
          <group position={[0, 0, 36]}>
            <mesh position={[0, -5, 0]}>
              <cylinderGeometry args={[0.02, 0.02, 10]} />
              <meshStandardMaterial color="#94a3b8" />
            </mesh>
            {/* Clamshell Bucket Blockout */}
            <group position={[0, -10, 0]} rotation={[-0.7, 0, 0]}>
              {/* Heavy guide frame */}
              <mesh castShadow>
                <boxGeometry args={[1.5, 3.5, 1]} />
                <meshStandardMaterial color="#3f3f46" roughness={0.8} metalness={0.7} />
              </mesh>
              {/* Left Jaw */}
              <mesh position={[-0.4, -2, 0]} rotation={[0, 0, -0.2]} castShadow>
                <boxGeometry args={[0.8, 1.5, 1.2]} />
                <meshStandardMaterial color="#27272a" roughness={0.9} metalness={0.8} />
              </mesh>
              {/* Right Jaw */}
              <mesh position={[0.4, -2, 0]} rotation={[0, 0, 0.2]} castShadow>
                <boxGeometry args={[0.8, 1.5, 1.2]} />
                <meshStandardMaterial color="#27272a" roughness={0.9} metalness={0.8} />
              </mesh>
              {/* Bentonite Slurry Drip FX */}
              <mesh position={[0, -3.2, 0]}>
                <cylinderGeometry args={[0.3, 0.1, 1.5]} />
                <meshPhysicalMaterial color="#a3a3a3" transmission={0.4} roughness={0.2} ior={1.3} thickness={0.5} />
              </mesh>
            </group>
          </group>
        </group>
      </group>

      {/* Excavator (Backhoe) */}
      <group position={[5.5, 0, 2.5]} rotation={[0, -0.6, 0]}>
        <group position={[0, 0.6, 0]}>
          <mesh position={[-1.2, 0, 0]} castShadow>
            <boxGeometry args={[0.6, 1, 4]} />
            <meshStandardMaterial color="#27272a" />
          </mesh>
          <mesh position={[1.2, 0, 0]} castShadow>
            <boxGeometry args={[0.6, 1, 4]} />
            <meshStandardMaterial color="#27272a" />
          </mesh>
        </group>
        <group position={[0, 2.0, 0]} rotation={[0, 0.4, 0]}>
          <mesh castShadow>
            <boxGeometry args={[2.5, 2, 3]} />
            <meshStandardMaterial color="#eab308" />
          </mesh>
          <mesh position={[0.8, 0, 1.5]} castShadow>
            <boxGeometry args={[0.8, 1.5, 1]} />
            <meshStandardMaterial color="#020617" />
          </mesh>
          {/* Articulated Boom */}
          <mesh position={[0, -0.2, 2.5]} rotation={[-0.6, 0, 0]} castShadow>
            <boxGeometry args={[0.6, 4.5, 0.6]} />
            <meshStandardMaterial color="#ca8a04" />
          </mesh>
          <mesh position={[0, 1.8, 4.5]} rotation={[1.0, 0, 0]} castShadow>
            <boxGeometry args={[0.5, 3.5, 0.5]} />
            <meshStandardMaterial color="#ca8a04" />
          </mesh>
          {/* Bucket */}
          <mesh position={[0, 0, 5.5]} rotation={[0.5, 0, 0]} castShadow>
            <boxGeometry args={[1, 1, 1]} />
            <meshStandardMaterial color="#18181b" />
          </mesh>
        </group>
      </group>

      {/* Dump Truck */}
      <group position={[2.5, 0, 6.5]} rotation={[0, 1.8, 0]}>
        <mesh position={[0, 0.8, 0]} castShadow>
          <boxGeometry args={[2.2, 0.5, 7]} />
          <meshStandardMaterial color="#1e293b" />
        </mesh>
        {/* Wheels (10-wheeler) */}
        {[-2.5, 1.5, 2.8].map((z) => (
          <group key={`wheel-${z}`} position={[0, 0.7, z]}>
            <mesh position={[-1.2, 0, 0]} rotation={[0, 0, Math.PI / 2]} castShadow>
              <cylinderGeometry args={[0.7, 0.7, 0.4, 24]} />
              <meshStandardMaterial color="#0f172a" />
            </mesh>
            <mesh position={[1.2, 0, 0]} rotation={[0, 0, Math.PI / 2]} castShadow>
              <cylinderGeometry args={[0.7, 0.7, 0.4, 24]} />
              <meshStandardMaterial color="#0f172a" />
            </mesh>
          </group>
        ))}
        {/* Cab Detail */}
        <group position={[0, 2.2, 2.5]}>
          <mesh castShadow>
            <boxGeometry args={[2.4, 2, 1.8]} />
            <meshStandardMaterial color="#dc2626" roughness={0.6} />
          </mesh>
          {/* Windshield */}
          <mesh position={[0, 0.2, 0.95]}>
            <planeGeometry args={[2, 1]} />
            <meshStandardMaterial color="#020617" metalness={0.8} />
          </mesh>
          {/* Side Windows */}
          <mesh position={[1.21, 0.2, 0]}>
            <planeGeometry args={[1, 1]} />
            <meshStandardMaterial color="#020617" metalness={0.8} />
          </mesh>
          {/* Front Grill */}
          <mesh position={[0, -0.6, 0.95]}>
            <boxGeometry args={[1.5, 0.8, 0.1]} />
            <meshStandardMaterial color="#64748b" metalness={0.6} />
          </mesh>
        </group>
        {/* Dump Bed */}
        <mesh position={[0, 2.2, -1.2]} rotation={[0.2, 0, 0]} castShadow>
          <boxGeometry args={[2.5, 1.5, 5]} />
          <meshStandardMaterial color="#94a3b8" metalness={0.5} roughness={0.6} />
        </mesh>
      </group>

      {/* 3. WORKER SILHOUETTES (Human Forms) */}
      {[
        { pos: [3.5, 0, 5], rot: 0.5 },
        { pos: [4.0, 0, 4.5], rot: -0.2 }
      ].map((worker, i) => (
        <group key={`worker-${i}`} position={worker.pos as [number, number, number]} rotation={[0, worker.rot, 0]}>
          {/* Legs */}
          <mesh position={[-0.15, 0.5, 0]} castShadow>
            <cylinderGeometry args={[0.1, 0.1, 1]} />
            <meshStandardMaterial color="#1e3a8a" /> {/* Denim */}
          </mesh>
          <mesh position={[0.15, 0.5, 0]} castShadow>
            <cylinderGeometry args={[0.1, 0.1, 1]} />
            <meshStandardMaterial color="#1e3a8a" />
          </mesh>
          {/* Torso */}
          <mesh position={[0, 1.3, 0]} castShadow>
            <boxGeometry args={[0.5, 0.6, 0.3]} />
            <meshStandardMaterial color="#bbf7d0" /> {/* Flannel/Shirt */}
          </mesh>
          {/* Arms */}
          <mesh position={[-0.3, 1.3, 0]} rotation={[0, 0, 0.2]} castShadow>
            <cylinderGeometry args={[0.08, 0.08, 0.6]} />
            <meshStandardMaterial color="#bbf7d0" />
          </mesh>
          <mesh position={[0.3, 1.3, 0]} rotation={[0, 0, -0.2]} castShadow>
            <cylinderGeometry args={[0.08, 0.08, 0.6]} />
            <meshStandardMaterial color="#bbf7d0" />
          </mesh>
          {/* Head & Hard Hat */}
          <group position={[0, 1.7, 0]}>
            <mesh castShadow>
              <sphereGeometry args={[0.15]} />
              <meshStandardMaterial color="#fcd34d" /> /* Skin tone */
            </mesh>
            <mesh position={[0, 0.1, 0]} castShadow>
              <sphereGeometry args={[0.18, 16, 16, 0, Math.PI * 2, 0, Math.PI / 2]} />
              <meshStandardMaterial color="#facc15" /> /* Yellow hard hat */
            </mesh>
            <mesh position={[0, 0.1, 0.1]} castShadow>
              <boxGeometry args={[0.2, 0.05, 0.2]} />
              <meshStandardMaterial color="#facc15" /> /* Hat brim */
            </mesh>
          </group>
        </group>
      ))}
    </group>
  );
};
