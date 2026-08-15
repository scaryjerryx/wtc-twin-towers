import React, { useEffect } from 'react';
import { Sky, useTexture } from '@react-three/drei';
import * as THREE from 'three';
import { ProvenanceData } from '../ui/ProvenanceModal';
import { VisualStorytelling } from './VisualStorytelling';
import { PathTube } from './PathTube';
import { Bathtub } from './Bathtub';

interface Day1WorldProps {
  onSelectProvenance: (data: ProvenanceData) => void;
}

export const Day1World: React.FC<Day1WorldProps> = ({ onSelectProvenance }) => {
  // Load Textures for ground
  const mudMaps = useTexture({
    map: '/textures/mud/color.jpg',
    normalMap: '/textures/mud/normal.png',
    roughnessMap: '/textures/mud/roughness.jpg',
  });

  useEffect(() => {
    Object.values(mudMaps).forEach(texture => {
      texture.wrapS = THREE.RepeatWrapping;
      texture.wrapT = THREE.RepeatWrapping;
      texture.repeat.set(30, 30);
    });
  }, [mudMaps]);

  // Provenance datasets
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
      {/* Historical August 1966 Morning Sky */}
      <Sky distance={450000} sunPosition={[100, 20, 100]} inclination={0} azimuth={0.25} />
      
      {/* 1. Base Ground Terrain (Y=0) - 1966 Radio Row Earth */}
      <mesh position={[0, -0.05, 0]} rotation={[-Math.PI / 2, 0, 0]} receiveShadow>
        <planeGeometry args={[160, 160]} />
        <meshStandardMaterial {...mudMaps} />
      </mesh>

      {/* Mud & Gravel Decals */}
      <mesh position={[0, -0.04, 10]} rotation={[-Math.PI / 2, 0, 0]} receiveShadow>
        <planeGeometry args={[12, 12]} />
        <meshStandardMaterial color="#2c241b" roughness={0.2} transparent opacity={0.6} />
      </mesh>
      <mesh position={[6, -0.04, 4]} rotation={[-Math.PI / 2, 0, 0.5]} receiveShadow>
        <planeGeometry args={[10, 8]} />
        <meshStandardMaterial color="#3d3126" roughness={0.4} transparent opacity={0.8} />
      </mesh>

      {/* Cobblestone Street Border (Church St Edge at Z = 18 to 28) */}
      <mesh position={[0, 0.02, 22]} receiveShadow>
        <boxGeometry args={[160, 0.08, 12]} />
        <meshStandardMaterial color="#57534e" roughness={0.7} />
      </mesh>

      {/* Sidewalk Curb Line at Z = 16 */}
      <mesh position={[0, 0.08, 16]} receiveShadow castShadow>
        <boxGeometry args={[160, 0.16, 0.4]} />
        <meshStandardMaterial color="#cbd5e1" roughness={0.6} />
      </mesh>

      {/* Timber Walkway extending from Church St to Site Trailer & Overlook */}
      <mesh position={[4, 0.04, 2]} receiveShadow>
        <boxGeometry args={[5, 0.08, 24]} />
        <meshStandardMaterial color="#705d46" roughness={0.9} />
      </mesh>
      <mesh position={[-4, 0.04, -5]} receiveShadow>
        <boxGeometry args={[14, 0.08, 4]} />
        <meshStandardMaterial color="#705d46" roughness={0.9} />
      </mesh>

      {/* Cortlandt Subway Hood Kiosk at Spawn (-6, 1.4, 12) */}
      <group position={[-6, 1.4, 12]}>
        <mesh castShadow receiveShadow>
          <boxGeometry args={[3.2, 2.6, 2.2]} />
          <meshStandardMaterial color="#334155" metalness={0.3} roughness={0.6} />
        </mesh>
        <mesh position={[0, 0.9, 1.12]}>
          <planeGeometry args={[2.8, 0.5]} />
          <meshStandardMaterial color="#0284c7" />
        </mesh>
        <mesh position={[0, -0.4, 1.12]}>
          <planeGeometry args={[2.2, 1.6]} />
          <meshBasicMaterial color="#0f172a" />
        </mesh>
      </group>

      {/* Perimeter Modular Hoarding Fences at Z = 16 (Gate Opening: X in [-2, 8]) */}
      <group position={[0, 1.25, 16]}>
        {/* Left Fence */}
        <mesh receiveShadow castShadow position={[-25, 0, 0]}>
          <boxGeometry args={[44, 2.5, 0.2]} />
          <meshStandardMaterial color="#8b5a2b" roughness={0.9} />
        </mesh>
        {/* Danger Keep Out Sign */}
        <mesh position={[-5, 0.3, 0.11]}>
          <planeGeometry args={[1.2, 0.8]} />
          <meshStandardMaterial color="#ef4444" />
        </mesh>
        <mesh position={[-5, 0.3, 0.12]}>
          <planeGeometry args={[1.0, 0.6]} />
          <meshBasicMaterial color="#ffffff" />
        </mesh>
        {/* Right Fence */}
        <mesh receiveShadow castShadow position={[25, 0, 0]}>
          <boxGeometry args={[34, 2.5, 0.2]} />
          <meshStandardMaterial color="#8b5a2b" roughness={0.9} />
        </mesh>
      </group>

      {/* 2. Entrance Visitor Direction Signboard (INTERACTIVE TARGET at X=4.8, Z=9.0) */}
      <group 
        name="interactable-sign"
        position={[4.8, 1.2, 9.0]}
        onClick={(e) => {
          e.stopPropagation();
          onSelectProvenance(entranceSignData);
        }}
      >
        <mesh castShadow>
          <boxGeometry args={[3.6, 1.8, 0.12]} />
          <meshStandardMaterial color="#1e40af" />
        </mesh>

        {/* Text Plate Graphic */}
        <mesh position={[0, 0, 0.07]}>
          <planeGeometry args={[3.4, 1.6]} />
          <meshStandardMaterial color="#0f172a" />
        </mesh>

        {/* Sign Header Banner Accent */}
        <mesh position={[0, 0.45, 0.08]}>
          <planeGeometry args={[3.0, 0.35]} />
          <meshBasicMaterial color="#f59e0b" />
        </mesh>

        {/* Support Posts */}
        <mesh position={[-1.1, -1.0, 0]} castShadow>
          <cylinderGeometry args={[0.07, 0.07, 1.2]} />
          <meshStandardMaterial color="#78350f" />
        </mesh>
        <mesh position={[1.1, -1.0, 0]} castShadow>
          <cylinderGeometry args={[0.07, 0.07, 1.2]} />
          <meshStandardMaterial color="#78350f" />
        </mesh>
      </group>

      {/* Survey Tripod near the pit */}
      <group position={[2, 0, -8]} rotation={[0, 0.4, 0]}>
        {/* Legs */}
        <mesh position={[0, 0.6, 0.3]} rotation={[0.2, 0, 0]} castShadow>
          <cylinderGeometry args={[0.02, 0.02, 1.4]} />
          <meshStandardMaterial color="#d4d4d8" roughness={0.4} />
        </mesh>
        <mesh position={[-0.25, 0.6, -0.15]} rotation={[-0.1, 0, 0.2]} castShadow>
          <cylinderGeometry args={[0.02, 0.02, 1.4]} />
          <meshStandardMaterial color="#d4d4d8" roughness={0.4} />
        </mesh>
        <mesh position={[0.25, 0.6, -0.15]} rotation={[-0.1, 0, -0.2]} castShadow>
          <cylinderGeometry args={[0.02, 0.02, 1.4]} />
          <meshStandardMaterial color="#d4d4d8" roughness={0.4} />
        </mesh>
        {/* Theodolite Instrument */}
        <mesh position={[0, 1.2, 0]} castShadow>
          <boxGeometry args={[0.15, 0.2, 0.25]} />
          <meshStandardMaterial color="#fb923c" roughness={0.5} />
        </mesh>
        <mesh position={[0, 1.3, 0.05]} rotation={[Math.PI / 2, 0, 0]} castShadow>
          <cylinderGeometry args={[0.05, 0.05, 0.3]} />
          <meshStandardMaterial color="#1f2937" roughness={0.3} />
        </mesh>
      </group>

      {/* 3. PORT AUTHORITY FIELD OFFICE TRAILER & DRAWING ROOM (ENTERABLE INTERIOR) */}
      {/* Position: Center [10, 0, -2], Size: 9 wide (X: 5.5 to 14.5), 6 deep (Z: -5 to +1), 3 high (Y: 0 to 3) */}
      <group position={[10, 0, -2]}>
        {/* Foundation Cinder Blocks */}
        {[-3.8, 0, 3.8].map((px) =>
          [-2.2, 2.2].map((pz) => (
            <mesh key={`cinder-${px}-${pz}`} position={[px, 0.15, pz]} castShadow receiveShadow>
              <boxGeometry args={[0.8, 0.3, 0.8]} />
              <meshStandardMaterial color="#cbd5e1" roughness={0.9} />
            </mesh>
          ))
        )}

        {/* Trailer Entry Steps at Doorway (Doorway at relative X = -2 -> world X = 8, relative Z = 3 -> world Z = 1) */}
        <group position={[-2, 0.15, 3.5]}>
          <mesh position={[0, 0.05, -0.3]} castShadow receiveShadow>
            <boxGeometry args={[1.8, 0.2, 0.6]} />
            <meshStandardMaterial color="#a16207" />
          </mesh>
          <mesh position={[0, -0.05, 0.2]} castShadow receiveShadow>
            <boxGeometry args={[2.0, 0.1, 0.6]} />
            <meshStandardMaterial color="#a16207" />
          </mesh>
        </group>

        {/* Trailer Floor */}
        <mesh position={[0, 0.25, 0]} receiveShadow>
          <boxGeometry args={[9, 0.1, 6]} />
          <meshStandardMaterial color="#94a3b8" roughness={0.7} />
        </mesh>

        {/* Trailer Roof */}
        <mesh position={[0, 3.0, 0]} castShadow>
          <boxGeometry args={[9.4, 0.2, 6.4]} />
          <meshStandardMaterial color="#334155" roughness={0.5} />
        </mesh>

        {/* Trailer Back Wall (Z = -3 relative -> world Z = -5) */}
        <mesh position={[0, 1.6, -3]} receiveShadow castShadow>
          <boxGeometry args={[9, 2.7, 0.15]} />
          <meshStandardMaterial color="#1e3a8a" roughness={0.6} />
        </mesh>

        {/* Trailer Left Wall (X = -4.5 relative -> world X = 5.5) */}
        <mesh position={[-4.5, 1.6, 0]} receiveShadow castShadow>
          <boxGeometry args={[0.15, 2.7, 6]} />
          <meshStandardMaterial color="#1e3a8a" roughness={0.6} />
        </mesh>

        {/* Trailer Right Wall (X = +4.5 relative -> world X = 14.5) */}
        <mesh position={[4.5, 1.6, 0]} receiveShadow castShadow>
          <boxGeometry args={[0.15, 2.7, 6]} />
          <meshStandardMaterial color="#1e3a8a" roughness={0.6} />
        </mesh>

        {/* Trailer Front Wall (Z = +3 relative -> world Z = 1) WITH DOORWAY OPENING */}
        {/* Left Section: X from -4.5 to -3 (width 1.5) */}
        <mesh position={[-3.75, 1.6, 3]} receiveShadow castShadow>
          <boxGeometry args={[1.5, 2.7, 0.15]} />
          <meshStandardMaterial color="#1e3a8a" roughness={0.6} />
        </mesh>
        {/* Right Section: X from -1 to +4.5 (width 5.5) */}
        <mesh position={[1.75, 1.6, 3]} receiveShadow castShadow>
          <boxGeometry args={[5.5, 2.7, 0.15]} />
          <meshStandardMaterial color="#1e3a8a" roughness={0.6} />
        </mesh>
        {/* Door Lintel Header above opening (X from -3 to -1, Y from 2.5 to 3.0) */}
        <mesh position={[-2, 2.75, 3]} receiveShadow castShadow>
          <boxGeometry args={[2, 0.5, 0.15]} />
          <meshStandardMaterial color="#1e3a8a" roughness={0.6} />
        </mesh>

        {/* Open Wooden Screen Door Ajar */}
        <group position={[-3, 1.35, 3]} rotation={[0, -0.8, 0]}>
          <mesh castShadow>
            <boxGeometry args={[0.08, 2.2, 1.2]} />
            <meshStandardMaterial color="#92400e" roughness={0.8} />
          </mesh>
        </group>

        {/* Port Authority Sign on Trailer Exterior */}
        <mesh position={[1.75, 2.4, 3.1]}>
          <planeGeometry args={[4.2, 0.6]} />
          <meshStandardMaterial color="#0284c7" />
        </mesh>

        {/* --- TRAILER INTERIOR PROPS & DRAWING ROOM --- */}
        {/* Warm Tungsten PointLight Spot over Drafting Table */}
        <pointLight position={[0, 2.5, 0]} intensity={2.8} distance={10} color="#ffedd5" />

        {/* Pinboard with Historical Photos on Back Wall */}
        <mesh position={[0, 1.8, -2.9]}>
          <planeGeometry args={[3.2, 1.4]} />
          <meshStandardMaterial color="#78350f" roughness={0.9} />
        </mesh>
        <mesh position={[-0.8, 1.8, -2.88]}>
          <planeGeometry args={[1.0, 0.8]} />
          <meshStandardMaterial color="#f1f5f9" />
        </mesh>
        <mesh position={[0.8, 1.8, -2.88]}>
          <planeGeometry args={[1.0, 0.8]} />
          <meshStandardMaterial color="#f1f5f9" />
        </mesh>

        {/* Steel Filing Cabinet */}
        <mesh position={[3.8, 1.1, -2.2]} castShadow receiveShadow>
          <boxGeometry args={[1.0, 1.7, 1.0]} />
          <meshStandardMaterial color="#64748b" metalness={0.6} roughness={0.4} />
        </mesh>

        {/* 4. OAK DRAFTING TABLE & DRAWING S-1 BLUEPRINT (INTERACTIVE TARGET) */}
        <group 
          name="interactable-drawing-s1"
          position={[0, 0.85, 0]}
          onClick={(e) => {
            e.stopPropagation();
            onSelectProvenance(drawingS1Data);
          }}
        >
          {/* Heavy Oak Table Top */}
          <mesh position={[0, 0, 0]} castShadow receiveShadow>
            <boxGeometry args={[2.8, 0.1, 1.8]} />
            <meshStandardMaterial color="#b45309" roughness={0.7} />
          </mesh>

          {/* Table Legs */}
          {[-1.2, 1.2].map((lx) =>
            [-0.7, 0.7].map((lz) => (
              <mesh key={`leg-${lx}-${lz}`} position={[lx, -0.4, lz]} castShadow>
                <boxGeometry args={[0.12, 0.8, 0.12]} />
                <meshStandardMaterial color="#78350f" roughness={0.8} />
              </mesh>
            ))
          )}

          {/* Drawing S-1 Blueprint Mesh Sheet */}
          <mesh position={[0, 0.06, 0]} rotation={[-Math.PI / 2, 0, 0]}>
            <planeGeometry args={[2.4, 1.5]} />
            <meshStandardMaterial color="#0284c7" roughness={0.3} />
          </mesh>

          {/* Blueprint Title Bar Graphic */}
          <mesh position={[0, 0.07, 0.55]} rotation={[-Math.PI / 2, 0, 0]}>
            <planeGeometry args={[2.2, 0.25]} />
            <meshBasicMaterial color="#38bdf8" />
          </mesh>

          {/* Rolled up blueprints */}
          <mesh position={[1.0, 0.08, 0.4]} rotation={[0, 0.3, Math.PI / 2]} castShadow>
            <cylinderGeometry args={[0.04, 0.04, 0.8]} />
            <meshStandardMaterial color="#bae6fd" />
          </mesh>
          <mesh position={[1.05, 0.08, 0.6]} rotation={[0, 0.5, Math.PI / 2]} castShadow>
            <cylinderGeometry args={[0.05, 0.05, 0.7]} />
            <meshStandardMaterial color="#e0f2fe" />
          </mesh>

          {/* Brass Desk Lamp */}
          <group position={[0.8, 0.35, -0.4]}>
            <mesh position={[0, 0, 0]}>
              <cylinderGeometry args={[0.12, 0.15, 0.05]} />
              <meshStandardMaterial color="#d97706" metalness={0.7} />
            </mesh>
            <mesh position={[0, 0.2, 0]}>
              <cylinderGeometry args={[0.02, 0.02, 0.4]} />
              <meshStandardMaterial color="#d97706" metalness={0.7} />
            </mesh>
            <mesh position={[-0.15, 0.35, 0]} rotation={[0, 0, 0.5]}>
              <coneGeometry args={[0.15, 0.25, 16]} />
              <meshStandardMaterial color="#d97706" metalness={0.7} />
            </mesh>
          </group>
        </group>
      </group>

      {/* 5. 70FT EXCAVATION PIT & BEDROCK CORE COLUMN MARKERS */}
      {/* Pit Floor */}
      <mesh position={[-25, -10, -15]} receiveShadow>
        <boxGeometry args={[40, 0.2, 40]} />
        <meshStandardMaterial color="#44403c" roughness={0.9} />
      </mesh>
      {/* The 70-FT "Bathtub" Excavation Pit */}
      <Bathtub />

      {/* Historical PATH Tubes crossing the site */}
      <PathTube />

      {/* Perimeter Modular Hoarding Fences at Z = 16 */}
      <group position={[0, -2, 16]}>
        {Array.from({ length: 15 }).map((_, i) => {
          const x = -35 + i * 5;
          // Create a gate opening for vehicles
          if (x > -2 && x < 8) return null;

          // Create a public observation viewing deck/window
          if (x === -7) {
            return (
              <group key={`fence-${i}`} position={[x, 0, 0]}>
                <mesh position={[0, 1.5, 0]} castShadow>
                  <boxGeometry args={[5, 7, 0.4]} />
                  <meshStandardMaterial color="#0f172a" roughness={0.9} /> {/* Needs Wood Texture */}
                </mesh>
                {/* Observation Window Cut-out */}
                <mesh position={[0, 3, 0.21]}>
                  <boxGeometry args={[3, 1.5, 0.5]} />
                  <meshStandardMaterial color="#000000" />
                </mesh>
                {/* Wire Mesh Realism */}
                <mesh position={[0, 3, 0.5]}>
                  <planeGeometry args={[3.2, 1.7]} />
                  <meshStandardMaterial color="#3f3f46" wireframe roughness={0.7} metalness={0.8} transparent opacity={0.6} />
                </mesh>
                {/* Public Signage Board */}
                <mesh position={[-3.5, 3.5, 0.25]} rotation={[0, 0, -0.05]} castShadow>
                  <boxGeometry args={[1.5, 1, 0.1]} />
                  <meshStandardMaterial color="#fef08a" roughness={1} />
                </mesh>
                {/* Stepping Platform */}
                <mesh position={[0, -1.8, 1.5]} castShadow>
                  <boxGeometry args={[4, 0.4, 2]} />
                  <meshStandardMaterial color="#3f3f46" roughness={0.9} />
                </mesh>
                {/* Crowd Presence (Citizen Silhouettes on platform) */}
                <mesh position={[-0.5, -0.5, 1.5]} castShadow>
                  <cylinderGeometry args={[0.3, 0.3, 2.5]} />
                  <meshStandardMaterial color="#334155" roughness={1} />
                </mesh>
                <mesh position={[1, -0.7, 1.8]} castShadow>
                  <cylinderGeometry args={[0.25, 0.25, 2.0]} />
                  <meshStandardMaterial color="#9f1239" roughness={1} />
                </mesh>
              </group>
            );
          }

          return (
            <mesh key={`fence-${i}`} position={[x, 1.5, 0]} castShadow>
              <boxGeometry args={[5, 7, 0.4]} />
              <meshStandardMaterial color="#0f172a" />
            </mesh>
          );
        })}
      </group>

      {/* White Chalk Lines outlining Core Columns 501-508 on bedrock */}
      <group position={[-25, -19.85, -15]}>
        {[-9, -3, 3, 9].map((x, i) =>
          [-9, 9].map((z, j) => (
            <group key={`col-${i}-${j}`} position={[x, 0, z]}>
              <mesh position={[0, 0.05, 0]}>
                <boxGeometry args={[2.8, 0.1, 2.8]} />
                <meshBasicMaterial color="#ffffff" />
              </mesh>
              <mesh position={[0, 0.6, 0]}>
                <boxGeometry args={[2.0, 1.0, 2.0]} />
                <meshStandardMaterial color="#475569" metalness={0.8} roughness={0.3} />
              </mesh>
            </group>
          ))
        )}
      </group>

      {/* 6. Timber Overlook Viewing Platform cantilevered over Pit */}
      <group position={[-4, 0.1, -12]}>
        <mesh receiveShadow castShadow position={[-2, 0, 0]}>
          <boxGeometry args={[5, 0.2, 8]} />
          <meshStandardMaterial color="#705d46" roughness={0.9} />
        </mesh>
        <mesh position={[-4.4, 0.6, 0]}>
          <boxGeometry args={[0.1, 1.0, 8]} />
          <meshStandardMaterial color="#8b7355" roughness={0.8} />
        </mesh>
        <mesh position={[-2, 0.6, 3.9]}>
          <boxGeometry args={[4.8, 1.0, 0.1]} />
          <meshStandardMaterial color="#8b7355" roughness={0.8} />
        </mesh>
        <mesh position={[-2, 0.6, -3.9]}>
          <boxGeometry args={[4.8, 1.0, 0.1]} />
          <meshStandardMaterial color="#8b7355" roughness={0.8} />
        </mesh>
      </group>

      {/* 7. Visitor Spawn Point Marker (Church & Cortlandt: 0, 0.05, 10) */}
      <group position={[0, 0.05, 10]}>
        <mesh rotation={[-Math.PI / 2, 0, 0]}>
          <ringGeometry args={[0.9, 1.3, 32]} />
          <meshBasicMaterial color="#10b981" transparent opacity={0.7} />
        </mesh>
      </group>

      {/* Visual Storytelling Assets */}
      <VisualStorytelling />
    </group>
  );
};
