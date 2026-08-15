import { useState } from 'react';
import { ExperienceCanvas } from './components/canvas/ExperienceCanvas';
import { HUD } from './components/ui/HUD';
import { ProvenanceModal, ProvenanceData } from './components/ui/ProvenanceModal';
import { Info, X, Footprints, MousePointer } from 'lucide-react';

export default function App() {
  const [selectedProvenance, setSelectedProvenance] = useState<ProvenanceData | null>(null);
  const [showVisionInfo, setShowVisionInfo] = useState<boolean>(false);
  const [hoveredTarget, setHoveredTarget] = useState<string | null>(null);

  const isModalActive = !!selectedProvenance || showVisionInfo;

  return (
    <div style={{ width: '100vw', height: '100vh', position: 'relative', overflow: 'hidden' }}>
      {/* 3D WebGL First-Person Canvas */}
      <ExperienceCanvas 
        onSelectProvenance={(data) => setSelectedProvenance(data)} 
        isModalOpen={isModalActive}
        onHoverTargetChange={(target) => setHoveredTarget(target)}
      />

      {/* Center Crosshair (visible when navigating in first-person mode) */}
      {!isModalActive && (
        <div 
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            pointerEvents: 'none',
            zIndex: 50,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            width: '24px',
            height: '24px'
          }}
        >
          <div 
            style={{
              width: hoveredTarget ? '10px' : '4px',
              height: hoveredTarget ? '10px' : '4px',
              borderRadius: '50%',
              backgroundColor: hoveredTarget ? '#38bdf8' : 'rgba(255, 255, 255, 0.7)',
              boxShadow: hoveredTarget ? '0 0 10px #38bdf8' : '0 0 4px rgba(0,0,0,0.5)',
              transition: 'all 0.15s ease'
            }} 
          />
        </div>
      )}

      {/* 2D HUD UI Overlay */}
      <HUD 
        onShowInfo={() => setShowVisionInfo(true)} 
        hoveredTarget={hoveredTarget}
      />

      {/* Provenance Inspection Modal */}
      <ProvenanceModal 
        data={selectedProvenance} 
        onClose={() => setSelectedProvenance(null)} 
      />

      {/* Project Vision & Controls Modal */}
      {showVisionInfo && (
        <div 
          className="interactive"
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            zIndex: 2000,
            maxWidth: '540px',
            width: '90%'
          }}
        >
          <div className="hud-card" style={{ padding: '24px', background: 'rgba(15, 23, 42, 0.96)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '16px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <Info color="#f59e0b" size={24} />
                <h3 style={{ margin: 0, fontSize: '18px', fontWeight: 700 }}>Day 1 (1966) First-Person Navigation</h3>
              </div>
              <button 
                onClick={() => setShowVisionInfo(false)}
                style={{ background: 'transparent', border: 'none', color: '#9ca3af', cursor: 'pointer' }}
              >
                <X size={20} />
              </button>
            </div>

            <div style={{ fontSize: '13px', color: '#cbd5e1', lineHeight: '1.6' }}>
              <p style={{ margin: '0 0 14px 0' }}>
                <strong>Living Historical Reconstruction (1966–2001):</strong> You stand in lower Manhattan on August 5, 1966. Explore the Radio Row demolition zone, inspect the 70ft bedrock excavation pit, and enter the Port Authority field office trailer.
              </p>
              
              <div style={{ background: 'rgba(255,255,255,0.05)', borderRadius: '8px', padding: '12px 14px', marginBottom: '14px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px', color: '#38bdf8', fontWeight: 600 }}>
                  <Footprints size={16} /> Movement Controls:
                </div>
                <ul style={{ margin: 0, paddingLeft: '20px', color: '#e2e8f0' }}>
                  <li><strong>WASD / Arrow Keys:</strong> Walk across the site</li>
                  <li><strong>Shift:</strong> Sprint / Fast walk</li>
                  <li><strong>Mouse:</strong> Click anywhere on the scene to lock mouse look (PointerLock)</li>
                  <li><strong>ESC:</strong> Release mouse pointer lock</li>
                </ul>
              </div>

              <div style={{ background: 'rgba(255,255,255,0.05)', borderRadius: '8px', padding: '12px 14px', marginBottom: '14px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '8px', marginBottom: '6px', color: '#10b981', fontWeight: 600 }}>
                  <MousePointer size={16} /> Evidence Inspection:
                </div>
                <p style={{ margin: 0, color: '#e2e8f0' }}>
                  Approach the <strong>Port Authority Site Trailer</strong> at the east of the site, step through the screen doorway into the drawing room, and click or press <strong>[E]</strong> on <strong>Drawing S-1</strong> on the drafting table to inspect the authoritative PANYNJ blueprint.
                </p>
              </div>

              <p style={{ margin: 0, fontSize: '12px', color: '#f59e0b' }}>
                *Governed by Vision Constitution 001 — The Experience is Primary.*
              </p>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
