import React, { useEffect } from 'react';
import { useTexture } from '@react-three/drei';
import * as THREE from 'three';
import { ChromaKeySprite } from './ChromaKeySprite';

export const Bathtub: React.FC = () => {
  // Dimensions
  const pitWidth = 50; // Z-axis width
  const pitLength = 50; // X-axis length
  const pitDepth = 20; // Y-axis depth (~70 feet)
  const panelWidth = 6.7; // ~22 feet per slurry panel pour

  // Number of panels per wall
  const numPanelsX = Math.ceil(pitLength / panelWidth);
  const numPanelsZ = Math.ceil(pitWidth / panelWidth);

  // Tie-back grid spacing
  const tieBackRows = 4; // 4 rows of tie-backs vertically
  const tieBacksPerPanel = 2; // 2 tie-backs horizontally per 22-ft panel

  // Load Textures
  const mudMaps = useTexture({
    map: '/textures/mud/color.jpg',
    normalMap: '/textures/mud/normal.png',
    roughnessMap: '/textures/mud/roughness.jpg',
  });
  const concreteMaps = useTexture({
    map: '/textures/concrete/Concrete015_2K-JPG_Color.jpg',
    normalMap: '/textures/concrete/Concrete015_2K-JPG_NormalGL.jpg',
    roughnessMap: '/textures/concrete/Concrete015_2K-JPG_Roughness.jpg',
  });
  const bedrockMaps = useTexture({
    map: '/textures/bedrock/Rock035_2K-JPG_Color.jpg',
    normalMap: '/textures/bedrock/Rock035_2K-JPG_NormalGL.jpg',
    roughnessMap: '/textures/bedrock/Rock035_2K-JPG_Roughness.jpg',
  });
  const metalMaps = useTexture({
    map: '/textures/metal/Metal035_1K-JPG_Color.jpg',
    normalMap: '/textures/metal/Metal035_1K-JPG_NormalGL.jpg',
    roughnessMap: '/textures/metal/Metal035_1K-JPG_Roughness.jpg',
    metalnessMap: '/textures/metal/Metal035_1K-JPG_Metalness.jpg',
  });

  useEffect(() => {
    [mudMaps, concreteMaps, bedrockMaps, metalMaps].forEach(maps => {
      Object.values(maps).forEach(texture => {
        texture.wrapS = THREE.RepeatWrapping;
        texture.wrapT = THREE.RepeatWrapping;
      });
    });
    // Set repetitions based on scale
    Object.values(mudMaps).forEach(t => t.repeat.set(10, 10));
    Object.values(bedrockMaps).forEach(t => t.repeat.set(5, 5));
    // Metal is small so maybe no repeat needed, or 1x1 is fine.
    // Concrete we tile dynamically in the material or just set it here? 
    // Wait, concrete wall is reused. If we set repeat here, it applies to all walls.
    // Let's set it to 1, 3 for concrete panel since panel is 6.7 wide x 20 high.
    Object.values(concreteMaps).forEach(t => t.repeat.set(1, 3));
  }, [mudMaps, concreteMaps, bedrockMaps, metalMaps]);


  const renderWall = (isXAxis: boolean, positionOffset: [number, number, number], numPanels: number) => {
    return (
      <group position={positionOffset}>
        {Array.from({ length: numPanels }).map((_, i) => {
          const offset = (- (numPanels * panelWidth) / 2) + (i * panelWidth) + (panelWidth / 2);
          const posX = isXAxis ? offset : 0;
          const posZ = isXAxis ? 0 : offset;

          return (
            <group key={`panel-${i}`} position={[posX, 0, posZ]}>
              {/* Main Concrete Panel */}
              <mesh position={[0, -pitDepth / 2, 0]} receiveShadow castShadow>
                <boxGeometry args={[isXAxis ? panelWidth - 0.1 : 0.6, pitDepth, isXAxis ? 0.6 : panelWidth - 0.1]} />
                <meshStandardMaterial {...concreteMaps} />
              </mesh>
              
              {/* Panel Seam (darker gap) */}
              <mesh position={[isXAxis ? panelWidth / 2 : 0, -pitDepth / 2, isXAxis ? 0 : panelWidth / 2]} receiveShadow>
                <boxGeometry args={[isXAxis ? 0.1 : 0.6, pitDepth, isXAxis ? 0.6 : 0.1]} />
                <meshStandardMaterial color="#334155" roughness={1.0} />
              </mesh>

              {/* Tie-back Anchor Grid */}
              {Array.from({ length: tieBackRows }).map((_, rowIdx) => {
                const yPos = -4 - (rowIdx * 4); // Rows starting from near top down to bottom
                return Array.from({ length: tieBacksPerPanel }).map((_, colIdx) => {
                  const localOffset = (-panelWidth / 4) + (colIdx * (panelWidth / 2));
                  const tX = isXAxis ? localOffset : (positionOffset[0] > 0 ? -0.3 : 0.3);
                  const tZ = isXAxis ? (positionOffset[2] > 0 ? -0.3 : 0.3) : localOffset;
                  
                  // Angles for the protruding caps (pointing slightly down and out)
                  const rotX = isXAxis ? (positionOffset[2] > 0 ? Math.PI/4 : -Math.PI/4) : 0;
                  const rotZ = isXAxis ? 0 : (positionOffset[0] > 0 ? -Math.PI/4 : Math.PI/4);

                  return (
                    <mesh key={`tieback-${rowIdx}-${colIdx}`} position={[tX, yPos, tZ]} rotation={[rotX, 0, rotZ]} castShadow>
                      <cylinderGeometry args={[0.3, 0.3, 0.5, 16]} />
                      <meshStandardMaterial {...metalMaps} /> {/* Iron caps */}
                    </mesh>
                  );
                });
              })}
            </group>
          );
        })}
      </group>
    );
  };

  return (
    <group position={[-25, 0, -15]}>
      {/* 1. Manhattan Schist Bedrock Floor */}
      {/* Creating a rough, uneven floor using slightly offset overlapping boxes */}
      <group position={[0, -pitDepth, 0]}>
        <mesh receiveShadow>
          <boxGeometry args={[pitLength, 1, pitWidth]} />
          <meshStandardMaterial {...mudMaps} />
        </mesh>
        {/* Jagged bedrock details (Highly realistic proxy) */}
        {Array.from({ length: 30 }).map((_, i) => (
          <mesh 
            key={`rock-${i}`} 
            position={[(Math.random() - 0.5) * pitLength, 0.2, (Math.random() - 0.5) * pitWidth]} 
            rotation={[Math.random() * Math.PI, Math.random() * Math.PI, Math.random() * Math.PI]} 
            scale={[Math.random() * 0.5 + 0.3, Math.random() * 0.3 + 0.2, Math.random() * 0.5 + 0.3]}
            receiveShadow castShadow
          >
            <icosahedronGeometry args={[1, 1]} />
            <meshStandardMaterial {...bedrockMaps} />
          </mesh>
        ))}
        {/* Groundwater Puddles (Highly Realistic Water) */}
        {Array.from({ length: 8 }).map((_, i) => (
          <mesh 
            key={`puddle-${i}`} 
            position={[(Math.random() - 0.5) * (pitLength-5), 0.52, (Math.random() - 0.5) * (pitWidth-5)]} 
            rotation={[0, Math.random() * Math.PI, 0]} 
            scale={[1, 0.05, 0.6 + Math.random() * 0.4]}
            receiveShadow
          >
            <cylinderGeometry args={[Math.random() * 2 + 1.5, Math.random() * 2 + 1.5, 1, 16]} />
            <meshStandardMaterial color="#0f172a" roughness={0.05} metalness={0.9} transparent opacity={0.8} />
          </mesh>
        ))}
      </group>

      {/* 2. Slurry Walls (North, South, East, West) */}
      {renderWall(true, [0, 0, -pitWidth / 2], numPanelsX)} {/* North Wall */}
      {renderWall(true, [0, 0, pitWidth / 2], numPanelsX)}  {/* South Wall */}
      {renderWall(false, [-pitLength / 2, 0, 0], numPanelsZ)} {/* West Wall */}
      {renderWall(false, [pitLength / 2, 0, 0], numPanelsZ)}  {/* East Wall */}
      
      {/* 3. SCALE REFERENCE: Street-level Timber Hoarding at the Rim */}
      <group position={[0, 1.25, 0]}>
        {/* North Rim */}
        <mesh position={[0, 0, -pitWidth / 2]} castShadow receiveShadow>
          <boxGeometry args={[pitLength, 2.5, 0.2]} />
          <meshStandardMaterial color="#c2a077" roughness={0.9} emissive="#402a15" />
        </mesh>
        {/* South Rim */}
        <mesh position={[0, 0, pitWidth / 2]} castShadow receiveShadow>
          <boxGeometry args={[pitLength, 2.5, 0.2]} />
          <meshStandardMaterial color="#c2a077" roughness={0.9} emissive="#402a15" />
        </mesh>
        {/* West Rim */}
        <mesh position={[-24.5, 1.25, 0]} castShadow receiveShadow>
          <boxGeometry args={[0.6, 2.5, pitWidth]} />
          <meshStandardMaterial color="#8b4513" roughness={1.0} emissive="#8b4513" emissiveIntensity={0.5} />
        </mesh>
        {/* East Rim */}
        <mesh position={[pitLength / 2, 0, 0]} castShadow receiveShadow>
          <boxGeometry args={[0.2, 2.5, pitWidth]} />
          <meshStandardMaterial color="#fcd34d" roughness={0.9} emissive="#f59e0b" emissiveIntensity={1.5} />
        </mesh>
      </group>

      {/* Lighting for the pit */}
      <ambientLight intensity={1.5} />
      <directionalLight position={[0, 100, 0]} intensity={3.5} castShadow />

      {/* 4. SCALE REFERENCE: Crawler Crane on the pit floor (Photorealistic Cutout) */}
      <group position={[0, -pitDepth + 4, 0]} rotation={[0, 0, 0]}>
        <ChromaKeySprite 
          texturePath="/sprites/crane.jpg" 
          position={[0, 0, 0]} 
          scale={[16, 16, 1]} 
          isBillboard={true} 
        />
      </group>

      {/* 5. SCALE REFERENCE: Construction Worker on the pit floor (Photorealistic Cutout) */}
      <group position={[-12, -pitDepth + 0.9, 3]}>
        <ChromaKeySprite 
          texturePath="/sprites/worker.jpg" 
          position={[0, 0, 0]} 
          scale={[1.8, 1.8, 1]} 
          isBillboard={true} 
        />
      </group>
    </group>
  );
};
