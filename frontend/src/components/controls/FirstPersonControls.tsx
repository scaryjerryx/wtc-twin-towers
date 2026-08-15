import React, { useEffect, useRef } from 'react';
import { useThree, useFrame } from '@react-three/fiber';
import * as THREE from 'three';
import { useKeyboardControls } from '../../hooks/useKeyboardControls';
import { ProvenanceData } from '../ui/ProvenanceModal';

interface FirstPersonControlsProps {
  onSelectProvenance: (data: ProvenanceData) => void;
  isModalOpen: boolean;
  onHoverTargetChange?: (targetName: string | null) => void;
}

export const FirstPersonControls: React.FC<FirstPersonControlsProps> = ({
  onSelectProvenance,
  isModalOpen,
  onHoverTargetChange
}) => {
  const { camera, gl, scene } = useThree();
  const keys = useKeyboardControls();

  // Position and Physics: Spawn at Church & Cortlandt facing northeast towards trailer entrance
  const playerPos = useRef(new THREE.Vector3(0, 1.7, 10));
  const velocity = useRef(new THREE.Vector3());
  const euler = useRef(new THREE.Euler(0, -0.65, 0, 'YXZ'));
  const isLocked = useRef(false);

  // Raycasting for object interaction
  const raycaster = useRef(new THREE.Raycaster());
  const centerCoord = useRef(new THREE.Vector2(0, 0));
  const currentHovered = useRef<string | null>(null);

  // Key interactive world coordinates
  const tablePos = useRef(new THREE.Vector3(10, 0.85, -2));
  const signPos = useRef(new THREE.Vector3(4.8, 1.2, 9));

  // Expose global handles for testing and smooth cinematic recording
  useEffect(() => {
    (window as any).__setCameraState = (x: number, y: number, z: number, yaw: number, pitch: number) => {
      playerPos.current.set(x, y, z);
      euler.current.set(pitch, yaw, 0, 'YXZ');
      camera.position.copy(playerPos.current);
      camera.quaternion.setFromEuler(euler.current);
    };
    (window as any).__triggerDrawingS1 = () => triggerInteraction('drawing-s1');
  }, [camera]);

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

  useEffect(() => {
    camera.position.copy(playerPos.current);
    camera.rotation.order = 'YXZ';
    camera.quaternion.setFromEuler(euler.current);

    const domElement = gl.domElement;

    const handlePointerLockChange = () => {
      isLocked.current = document.pointerLockElement === domElement;
    };

    const handleMouseMove = (event: MouseEvent) => {
      if (!isLocked.current || isModalOpen) return;

      const movementX = event.movementX || 0;
      const movementY = event.movementY || 0;

      euler.current.y -= movementX * 0.0022;
      euler.current.x -= movementY * 0.0022;

      // Clamp vertical pitch (-85 deg to +85 deg)
      euler.current.x = Math.max(-Math.PI / 2.1, Math.min(Math.PI / 2.1, euler.current.x));

      camera.quaternion.setFromEuler(euler.current);
    };

    const handleClick = () => {
      if (isModalOpen) return;

      // Check if clicking near/on an interactable target
      if (currentHovered.current) {
        triggerInteraction(currentHovered.current);
        return;
      }
      if (playerPos.current.distanceTo(tablePos.current) < 4.0) {
        triggerInteraction('drawing-s1');
        return;
      }
      if (playerPos.current.distanceTo(signPos.current) < 4.0) {
        triggerInteraction('sign');
        return;
      }

      if (!isLocked.current) {
        domElement.requestPointerLock();
      }
    };

    const handleDirectKeyDown = (event: KeyboardEvent) => {
      if (event.code === 'KeyE' && !isModalOpen) {
        if (currentHovered.current) {
          triggerInteraction(currentHovered.current);
        } else if (playerPos.current.distanceTo(tablePos.current) < 4.0) {
          triggerInteraction('drawing-s1');
        } else if (playerPos.current.distanceTo(signPos.current) < 4.0) {
          triggerInteraction('sign');
        }
      }
    };

    document.addEventListener('pointerlockchange', handlePointerLockChange);
    document.addEventListener('mousemove', handleMouseMove);
    domElement.addEventListener('click', handleClick);
    window.addEventListener('keydown', handleDirectKeyDown);

    return () => {
      document.removeEventListener('pointerlockchange', handlePointerLockChange);
      document.removeEventListener('mousemove', handleMouseMove);
      domElement.removeEventListener('click', handleClick);
      window.removeEventListener('keydown', handleDirectKeyDown);
    };
  }, [camera, gl, isModalOpen]);

  // Release pointer lock if modal opens
  useEffect(() => {
    if (isModalOpen && document.pointerLockElement) {
      document.exitPointerLock();
      isLocked.current = false;
    }
  }, [isModalOpen]);

  const triggerInteraction = (objectName: string) => {
    if (objectName.includes('drawing')) {
      onSelectProvenance(drawingS1Data);
      if (document.pointerLockElement) {
        document.exitPointerLock();
      }
    } else if (objectName.includes('sign')) {
      onSelectProvenance(entranceSignData);
      if (document.pointerLockElement) {
        document.exitPointerLock();
      }
    }
  };

  // Check 'E' keypress interaction
  useEffect(() => {
    if (keys.interact && !isModalOpen) {
      if (currentHovered.current) {
        triggerInteraction(currentHovered.current);
      } else if (playerPos.current.distanceTo(tablePos.current) < 4.0) {
        triggerInteraction('drawing-s1');
      } else if (playerPos.current.distanceTo(signPos.current) < 4.0) {
        triggerInteraction('sign');
      }
    }
  }, [keys.interact, isModalOpen]);

  // Movement & Collision Loop
  useFrame((_, delta) => {
    if (isModalOpen) return;

    // Movement calculation
    const speed = keys.sprint ? 7.5 : 4.5;
    const moveDir = new THREE.Vector3();

    // Forward/backward relative to camera yaw
    const forwardVector = new THREE.Vector3(0, 0, -1).applyAxisAngle(new THREE.Vector3(0, 1, 0), euler.current.y);
    const rightVector = new THREE.Vector3(1, 0, 0).applyAxisAngle(new THREE.Vector3(0, 1, 0), euler.current.y);

    if (keys.forward) moveDir.add(forwardVector);
    if (keys.backward) moveDir.sub(forwardVector);
    if (keys.right) moveDir.add(rightVector);
    if (keys.left) moveDir.sub(rightVector);

    if (moveDir.lengthSq() > 0) {
      moveDir.normalize();
    }

    // Velocity with smooth damping
    const targetVel = moveDir.multiplyScalar(speed);
    velocity.current.lerp(targetVel, Math.min(1, delta * 12));

    const proposedPos = playerPos.current.clone().addScaledVector(velocity.current, delta);

    // Collision Boundaries
    // 1. World outer bounds
    proposedPos.x = Math.max(-65, Math.min(65, proposedPos.x));
    proposedPos.z = Math.max(-65, Math.min(20, proposedPos.z));

    // 2. Perimeter Hoarding Fence at Z = 16 (Gate opening: X in [-2, 8])
    const crossingFence = (playerPos.current.z > 16 && proposedPos.z <= 16) || (playerPos.current.z < 16 && proposedPos.z >= 16);
    if (crossingFence) {
      const inGate = proposedPos.x >= -2 && proposedPos.x <= 8;
      if (!inGate) {
        proposedPos.z = playerPos.current.z; // Block fence
      }
    }

    // 3. Excavation Pit Edge Collision (Pit: X in [-45.5, -4.5], Z in [-35.5, 5.5])
    // Allow standing on overlook platform near X in [-8, -2], Z in [-16, -8]
    const inExcavationPit = proposedPos.x > -45.5 && proposedPos.x < -4.5 && proposedPos.z > -35.5 && proposedPos.z < 5.5;
    const onOverlookCatwalk = proposedPos.x >= -8 && proposedPos.x <= -2 && proposedPos.z >= -16 && proposedPos.z <= -8;

    if (inExcavationPit && !onOverlookCatwalk) {
      if (playerPos.current.x >= -4.5) proposedPos.x = Math.max(-4.4, proposedPos.x);
      else if (playerPos.current.x <= -45.5) proposedPos.x = Math.min(-45.6, proposedPos.x);
      
      if (playerPos.current.z >= 5.5) proposedPos.z = Math.max(5.6, proposedPos.z);
      else if (playerPos.current.z <= -35.5) proposedPos.z = Math.min(-35.6, proposedPos.z);
    }

    // 4. Trailer Entry and Interior Bounds
    // Trailer footprint: X in [5.4, 14.6], Z in [-5.2, 1.2]
    // Doorway opening: X in [6.8, 9.2] at Z = 1.0
    const wasInsideTrailer = playerPos.current.x >= 5.6 && playerPos.current.x <= 14.4 &&
                            playerPos.current.z >= -5.0 && playerPos.current.z <= 1.0;

    const enteringThroughDoor = proposedPos.x >= 6.8 && proposedPos.x <= 9.2 &&
                                proposedPos.z >= 0.8 && proposedPos.z <= 1.3;

    if (wasInsideTrailer) {
      // Inside trailer: allow exiting only through doorway
      if (proposedPos.z > 1.0 && !enteringThroughDoor) {
        proposedPos.z = 0.95;
      }
      if (proposedPos.z < -4.8) proposedPos.z = -4.8;
      if (proposedPos.x < 5.7) proposedPos.x = 5.7;
      if (proposedPos.x > 14.3) proposedPos.x = 14.3;

      // Drafting table collision (Table at [10, 0.85, -2], Size: X in [8.5, 11.5], Z in [-3.0, -1.0])
      if (proposedPos.x >= 8.4 && proposedPos.x <= 11.6 && proposedPos.z >= -3.1 && proposedPos.z <= -0.9) {
        const dLeft = Math.abs(proposedPos.x - 8.4);
        const dRight = Math.abs(proposedPos.x - 11.6);
        const dFront = Math.abs(proposedPos.z - -0.9);
        const dBack = Math.abs(proposedPos.z - -3.1);
        const minD = Math.min(dLeft, dRight, dFront, dBack);

        if (minD === dLeft) proposedPos.x = 8.3;
        else if (minD === dRight) proposedPos.x = 11.7;
        else if (minD === dFront) proposedPos.z = -0.8;
        else proposedPos.z = -3.2;
      }
    } else {
      // Outside trailer
      const tryingToEnterTrailer = proposedPos.x >= 5.4 && proposedPos.x <= 14.6 &&
                                   proposedPos.z >= -5.2 && proposedPos.z <= 1.2;
      if (tryingToEnterTrailer && !enteringThroughDoor) {
        if (playerPos.current.z > 1.2) proposedPos.z = Math.max(1.3, proposedPos.z);
        else if (playerPos.current.z < -5.2) proposedPos.z = Math.min(-5.3, proposedPos.z);
        else if (playerPos.current.x < 5.4) proposedPos.x = Math.min(5.3, proposedPos.x);
        else if (playerPos.current.x > 14.6) proposedPos.x = Math.max(14.7, proposedPos.x);
      }
    }

    // Human eye height (1.7m or relative to pit floor)
    if (playerPos.current.y < 0) {
      proposedPos.y = playerPos.current.y;
    } else {
      proposedPos.y = 1.7;
    }
    playerPos.current.copy(proposedPos);
    camera.position.copy(playerPos.current);
    camera.quaternion.setFromEuler(euler.current);

    // Raycast center crosshair for interactable meshes
    raycaster.current.setFromCamera(centerCoord.current, camera);
    const intersects = raycaster.current.intersectObjects(scene.children, true);

    let foundTarget: string | null = null;
    for (const hit of intersects) {
      if (hit.distance > 5.5) break;

      let curr: THREE.Object3D | null = hit.object;
      while (curr && curr !== scene) {
        if (curr.name && (curr.name.includes('drawing') || curr.name.includes('sign'))) {
          foundTarget = curr.name;
          break;
        }
        curr = curr.parent;
      }
      if (foundTarget) break;
    }

    // Proximity fallback when standing next to drafting table
    if (!foundTarget && playerPos.current.distanceTo(tablePos.current) < 4.0) {
      foundTarget = 'interactable-drawing-s1';
    } else if (!foundTarget && playerPos.current.distanceTo(signPos.current) < 4.0) {
      foundTarget = 'interactable-sign';
    }

    currentHovered.current = foundTarget;
    if (onHoverTargetChange) {
      onHoverTargetChange(foundTarget);
    }
  });

  return null;
};
