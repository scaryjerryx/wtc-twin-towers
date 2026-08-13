import React from 'react';
import { Calendar, MapPin, Compass, HelpCircle } from 'lucide-react';

interface HUDProps {
  onShowInfo: () => void;
}

export const HUD: React.FC<HUDProps> = ({ onShowInfo }) => {
  return (
    <div className="ui-overlay">
      {/* Top Header Row */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <div className="hud-card interactive" style={{ maxWidth: '380px' }}>
          <div className="badge-tag">Day 1 / 35 (Year 1966)</div>
          <h2 style={{ margin: '0 0 6px 0', fontSize: '20px', fontWeight: 700, letterSpacing: '-0.5px' }}>
            World Trade Center
          </h2>
          <p style={{ margin: 0, fontSize: '13px', color: '#9ca3af', lineHeight: '1.4' }}>
            Radio Row Demolition & Slurry Wall Excavation Era
          </p>
          
          <div style={{ display: 'flex', gap: '16px', marginTop: '14px', fontSize: '12px', color: '#d1d5db' }}>
            <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <Calendar size={14} color="#f59e0b" />
              August 5, 1966
            </span>
            <span style={{ display: 'flex', alignItems: 'center', gap: '6px' }}>
              <MapPin size={14} color="#3b82f6" />
              Church & Cortlandt
            </span>
          </div>
        </div>

        <button 
          className="hud-card interactive"
          onClick={onShowInfo}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '8px',
            color: '#fff',
            cursor: 'pointer',
            border: '1px solid rgba(255,255,255,0.2)',
            fontSize: '13px'
          }}
        >
          <HelpCircle size={16} color="#f59e0b" />
          <span>Controls & Vision</span>
        </button>
      </div>

      {/* Bottom Footer Controls Prompt */}
      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <div className="hud-card" style={{ fontSize: '12px', color: '#d1d5db', textAlign: 'center' }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '8px' }}>
            <Compass size={14} color="#10b981" />
            <strong>Desktop Controls:</strong> Click to lock mouse look | WASD to Walk | Touch items to inspect provenance
          </span>
        </div>
      </div>
    </div>
  );
};
