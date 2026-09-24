import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import SearchModal from './components/SearchModal';
import HomePage from './pages/HomePage';
import CourseRoadmapPage from './pages/CourseRoadmapPage';
import TopicLearningPage from './pages/TopicLearningPage';
import CurrentAffairsPage from './pages/CurrentAffairsPage';
import AdminDashboardPage from './pages/AdminDashboardPage';
import ProfilePage from './pages/ProfilePage';
import OverallQuizPage from './pages/OverallQuizPage';
import GovernmentExamsPage from './pages/GovernmentExamsPage';
import NotesPage from './pages/NotesPage';

export default function App() {
  const [currentView, setCurrentView] = useState('home');
  const [viewParams, setViewParams] = useState({});
  const [isSearchOpen, setIsSearchOpen] = useState(false);

  // Keyboard shortcut Cmd/Ctrl + K for instant search
  useEffect(() => {
    const handleKeyDown = (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
        e.preventDefault();
        setIsSearchOpen(prev => !prev);
      }
      if (e.key === 'Escape') {
        setIsSearchOpen(false);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const navigateTo = (view, params = {}) => {
    setCurrentView(view);
    setViewParams(params);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="app-container">
      {/* Universal Header */}
      <Header 
        currentView={currentView}
        navigateTo={navigateTo}
        onOpenSearch={() => setIsSearchOpen(true)}
      />

      {/* Main Dynamic View */}
      <main className="main-content">
        {currentView === 'home' && (
          <HomePage navigateTo={navigateTo} />
        )}

        {currentView === 'course' && (
          <CourseRoadmapPage 
            slug={viewParams.slug || 'english'} 
            navigateTo={navigateTo} 
          />
        )}

        {currentView === 'topic' && (
          <TopicLearningPage 
            topicId={viewParams.id || 1} 
            navigateTo={navigateTo} 
          />
        )}

        {currentView === 'government-exams' && (
          <GovernmentExamsPage 
            navigateTo={navigateTo} 
            viewExamId={viewParams.examId} 
          />
        )}

        {currentView === 'notes' && (
          <NotesPage navigateTo={navigateTo} />
        )}

        {currentView === 'current-affairs' && (
          <CurrentAffairsPage navigateTo={navigateTo} />
        )}

        {currentView === 'overall-quiz' && (
          <OverallQuizPage navigateTo={navigateTo} />
        )}

        {currentView === 'admin' && (
          <AdminDashboardPage navigateTo={navigateTo} />
        )}

        {(currentView === 'profile' || currentView === 'progress') && (
          <ProfilePage navigateTo={navigateTo} />
        )}
      </main>

      {/* Universal Footer */}
      <Footer navigateTo={navigateTo} />

      {/* Global Search Modal */}
      <SearchModal 
        isOpen={isSearchOpen}
        onClose={() => setIsSearchOpen(false)}
        navigateTo={navigateTo}
      />
    </div>
  );
}
