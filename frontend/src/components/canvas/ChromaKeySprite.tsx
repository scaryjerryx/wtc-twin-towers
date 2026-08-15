import React from 'react';
import { useTexture, Billboard } from '@react-three/drei';
import * as THREE from 'three';

interface ChromaKeySpriteProps {
  texturePath: string;
  position: [number, number, number];
  scale: [number, number, number];
  rotation?: [number, number, number];
  isBillboard?: boolean;
}

export const ChromaKeySprite: React.FC<ChromaKeySpriteProps> = ({ texturePath, position, scale, rotation, isBillboard = true }) => {
  // Use PNG instead of JPG for transparency
  const resolvedPath = texturePath.replace('.jpg', '.png');
  const texture = useTexture(resolvedPath);
  texture.colorSpace = THREE.SRGBColorSpace;

  const content = (
    <mesh scale={scale} rotation={rotation || [0,0,0]}>
      <planeGeometry args={[1, 1]} />
      <meshBasicMaterial map={texture} transparent={true} side={THREE.DoubleSide} depthWrite={false} />
    </mesh>
  );

  if (isBillboard) {
    return (
      <Billboard position={position} follow={true} lockX={false} lockY={false} lockZ={false}>
        {content}
      </Billboard>
    );
  }

  return (
    <group position={position}>
      {content}
    </group>
  );
};
