import { useState } from 'react';
import { ExperienceCanvas } from './components/canvas/ExperienceCanvas';
import { HUD } from './components/ui/HUD';
import { ProvenanceModal, ProvenanceData } from './components/ui/ProvenanceModal';
import { Info, X } from 'lucide-react';

export default function App() {
  const [selectedProvenance, setSelectedProvenance] = useState<ProvenanceData | null>(null);
  const [showVisionInfo, setShowVisionInfo] = useState<boolean>(false);

  return (
    <div style={{ width: '100vw', height: '100vh', position: 'relative', overflow: 'hidden' }}>
      {/* 3D WebGL Canvas */}
      <ExperienceCanvas onSelectProvenance={(data) => setSelectedProvenance(data)} />

      {/* 2D HUD UI Overlay */}
      <HUD onShowInfo={() => setShowVisionInfo(true)} />

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
            maxWidth: '520px',
            width: '90%'
          }}
        >
          <div className="hud-card" style={{ padding: '24px', background: 'rgba(15, 23, 42, 0.95)' }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '16px' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
                <Info color="#f59e0b" size={24} />
                <h3 style={{ margin: 0, fontSize: '18px', fontWeight: 700 }}>Project Vision & Controls</h3>
              </div>
              <button 
                onClick={() => setShowVisionInfo(false)}
                style={{ background: 'transparent', border: 'none', color: '#9ca3af', cursor: 'pointer' }}
              >
                <X size={20} />
              </button>
            </div>

            <div style={{ fontSize: '13px', color: '#cbd5e1', lineHeight: '1.6' }}>
              <p style={{ margin: '0 0 12px 0' }}>
                <strong>The World Trade Center Experience:</strong> Step back in time to explore the World Trade Center Complex as it evolved day-by-day from 1966 to 2001.
              </p>
              <ul style={{ margin: '0 0 12px 0', paddingLeft: '20px', color: '#94a3b8' }}>
                <li><strong>Day 1 (1966):</strong> Radio Row Demolition & Slurry Wall Trench Excavation</li>
                <li><strong>Interaction:</strong> Click on blue items (e.g. Drawing S-1 on drafting table) to inspect authoritative blueprint evidence cards.</li>
                <li><strong>Navigation:</strong> Drag mouse to rotate view, scroll wheel to zoom, or use touch controls.</li>
              </ul>
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
