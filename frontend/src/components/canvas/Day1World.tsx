import React, { useState } from 'react';
import { ProvenanceData } from '../ui/ProvenanceModal';

interface Day1WorldProps {
  onSelectProvenance: (data: ProvenanceData) => void;
}

export const Day1World: React.FC<Day1WorldProps> = ({ onSelectProvenance }) => {
  const [hovered, setHovered] = useState<string | null>(null);

  // Provenance dataset for interactive objects
  const drawingS1Data: ProvenanceData = {
    title: 'Drawing S-1: Bedrock Excavation & Slurry Wall Plan',
    contractRef: 'NYA-110.001 (Port Authority NY & NJ)',
    date: 'Approved June 1966 | Active Execution August 1966',
    description: 'Depicts the 3,100-foot continuous bentonite slurry wall perimeter trench engineered by Icanda Ltd. to retain Hudson River water table during bedrock excavation.',
    evidenceType: 'AUTHORITATIVE',
    evidenceDetails: 'Directly digitized from PANYNJ Contract Series S-1. Core Box Columns 501-508 coordinate footings verified against 1966 bedrock survey logs.'
  };

  const entranceSignData: ProvenanceData = {
    title: 'Port Authority Site Entrance Signboard',
    contractRef: 'PANYNJ Radio Row Groundbreaking Record 1966',
    date: 'August 5, 1966',
    description: 'Historical site entry signboard erected along Church & Cortlandt Streets during Radio Row demolition and initial slurry wall trenching.',
    evidenceType: 'EVIDENCE-BACKED',
    evidenceDetails: 'Corroborated by PANYNJ Press Photography Collection #NYA-1966-0805.'
  };

  return (
    <group>
      {/* 1. Base Terrain Ground Plane (Y=0) */}
      <mesh position={[0, -0.05, 0]} receiveShadow>
        <planeGeometry args={[120, 120]} />
        <meshStandardMaterial color="#3d372e" roughness={0.9} />
      </mesh>

      {/* Cobblestone Street Border (Church St Edge) */}
      <mesh position={[0, 0, 25]} receiveShadow>
        <boxGeometry args={[120, 0.1, 10]} />
        <meshStandardMaterial color="#2b2b2b" roughness={0.7} />
      </mesh>

      {/* 2. 70ft Excavation Pit Depressions (Y = -5 to -15) */}
      <mesh position={[-20, -5, -15]} receiveShadow>
        <boxGeometry args={[40, 10, 40]} />
        <meshStandardMaterial color="#26211a" roughness={0.95} />
      </mesh>

      {/* White Chalk Lines outlining Core Columns 501-508 on bedrock */}
      <group position={[-20, -9.9, -15]}>
        {[-8, -3, 3, 8].map((x, i) => (
          [-8, 8].map((z, j) => (
            <mesh key={`col-${i}-${j}`} position={[x, 0.05, z]}>
              <boxGeometry args={[2.5, 0.1, 2.5]} />
              <meshBasicMaterial color="#ffffff" />
            </mesh>
          ))
        ))}
      </group>

      {/* 3. Bentonite Slurry Wall Trench Line along West Street */}
      <mesh position={[-40, -4, -15]} receiveShadow>
        <boxGeometry args={[2, 8, 42]} />
        <meshStandardMaterial color="#64748b" roughness={0.3} metalness={0.2} />
      </mesh>

      {/* 4. Modular Timber Hoarding Fences */}
      <group position={[0, 1.25, 20]}>
        <mesh receiveShadow castShadow>
          <boxGeometry args={[60, 2.5, 0.2]} />
          <meshStandardMaterial color="#854d0e" roughness={0.8} />
        </mesh>
      </group>

      {/* 5. Entrance Visitor Direction Signboard (INTERACTIVE TARGET) */}
      <group 
        position={[5, 1.2, 18]}
        onClick={(e) => {
          e.stopPropagation();
          onSelectProvenance(entranceSignData);
        }}
        onPointerOver={() => setHovered('sign')}
        onPointerOut={() => setHovered(null)}
      >
        <mesh castShadow>
          <boxGeometry args={[4, 1.8, 0.1]} />
          <meshStandardMaterial color={hovered === 'sign' ? '#f59e0b' : '#1e3a8a'} />
        </mesh>

        {/* Text Plate Graphic */}
        <mesh position={[0, 0, 0.06]}>
          <planeGeometry args={[3.8, 1.6]} />
          <meshStandardMaterial color="#0f172a" />
        </mesh>

        {/* Support Post */}
        <mesh position={[0, -1, 0]} castShadow>
          <cylinderGeometry args={[0.08, 0.08, 1.2]} />
          <meshStandardMaterial color="#451a03" />
        </mesh>
      </group>

      {/* 6. Port Authority Construction Field Office Trailer */}
      <group position={[15, 1.5, -5]}>
        {/* Main Body */}
        <mesh castShadow receiveShadow>
          <boxGeometry args={[10, 3, 6]} />
          <meshStandardMaterial color="#1e3a8a" roughness={0.6} />
        </mesh>
        {/* Roof */}
        <mesh position={[0, 1.6, 0]}>
          <boxGeometry args={[10.4, 0.2, 6.4]} />
          <meshStandardMaterial color="#0f172a" />
        </mesh>
        {/* Screen Door Frame */}
        <mesh position={[-2, -0.2, 3.05]}>
          <boxGeometry args={[1.2, 2.2, 0.1]} />
          <meshStandardMaterial color="#78350f" />
        </mesh>
      </group>

      {/* 7. Drawing Room & Drafting Table (Inside Trailer: INTERACTIVE TARGET) */}
      <group 
        position={[15, 0.9, -5]}
        onClick={(e) => {
          e.stopPropagation();
          onSelectProvenance(drawingS1Data);
        }}
        onPointerOver={() => setHovered('drawing')}
        onPointerOut={() => setHovered(null)}
      >
        {/* Oak Table */}
        <mesh position={[0, 0, 0]} castShadow>
          <boxGeometry args={[2.5, 0.8, 1.5]} />
          <meshStandardMaterial color="#92400e" roughness={0.7} />
        </mesh>
        {/* Drawing S-1 Blueprint Mesh */}
        <mesh position={[0, 0.42, 0]} rotation={[-Math.PI / 2, 0, 0]}>
          <planeGeometry args={[2.2, 1.3]} />
          <meshStandardMaterial color={hovered === 'drawing' ? '#60a5fa' : '#1d4ed8'} />
        </mesh>
      </group>

      {/* 8. Visitor Spawn Point Marker (Church & Cortlandt: 0, 0.1, 10) */}
      <group position={[0, 0.1, 10]}>
        <mesh rotation={[-Math.PI / 2, 0, 0]}>
          <ringGeometry args={[0.8, 1.2, 32]} />
          <meshBasicMaterial color="#10b981" transparent opacity={0.6} />
        </mesh>
      </group>
    </group>
  );
};
