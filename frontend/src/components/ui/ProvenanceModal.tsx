import React from 'react';
import { X, FileText, CheckCircle2 } from 'lucide-react';

export interface ProvenanceData {
  title: string;
  contractRef: string;
  date: string;
  description: string;
  evidenceType: 'AUTHORITATIVE' | 'EVIDENCE-BACKED' | 'INTERPRETIVE';
  evidenceDetails: string;
}

interface ProvenanceModalProps {
  data: ProvenanceData | null;
  onClose: () => void;
}

export const ProvenanceModal: React.FC<ProvenanceModalProps> = ({ data, onClose }) => {
  if (!data) return null;

  const isAuthoritative = data.evidenceType === 'AUTHORITATIVE';

  return (
    <div 
      className="interactive"
      style={{
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        zIndex: 1000,
        maxWidth: '480px',
        width: '90%'
      }}
    >
      <div className="hud-card" style={{ padding: '24px', background: 'rgba(15, 23, 42, 0.95)' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '16px' }}>
          <div>
            <span 
              className="badge-tag" 
              style={{ background: isAuthoritative ? '#059669' : '#d97706' }}
            >
              {data.evidenceType} EVIDENCE
            </span>
            <h3 style={{ margin: '4px 0 0 0', fontSize: '18px', fontWeight: 700 }}>{data.title}</h3>
          </div>
          <button 
            onClick={onClose}
            style={{ 
              background: 'transparent', 
              border: 'none', 
              color: '#9ca3af', 
              cursor: 'pointer',
              padding: '4px'
            }}
          >
            <X size={20} />
          </button>
        </div>

        <div style={{ fontSize: '13px', color: '#cbd5e1', display: 'flex', flexDirection: 'column', gap: '12px' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px', background: 'rgba(255,255,255,0.05)', padding: '8px 12px', borderRadius: '6px' }}>
            <FileText size={16} color="#3b82f6" />
            <div>
              <strong style={{ color: '#93c5fd' }}>PANYNJ Contract Ref:</strong> {data.contractRef}
            </div>
          </div>

          <p style={{ margin: 0, lineHeight: '1.5', color: '#e2e8f0' }}>{data.description}</p>

          <div style={{ borderTop: '1px solid rgba(255,255,255,0.1)', paddingTop: '12px', display: 'flex', gap: '8px' }}>
            <CheckCircle2 size={16} color="#10b981" style={{ flexShrink: 0, marginTop: '2px' }} />
            <span style={{ fontSize: '12px', color: '#94a3b8' }}>
              <strong style={{ color: '#f8fafc' }}>Provenance Basis:</strong> {data.evidenceDetails}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};
