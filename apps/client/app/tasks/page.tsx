'use client';

import { useState, useEffect } from 'react';
import { api, Task } from '../../lib/api';
import TaskItem from '../../components/task/TaskItem';
import TaskForm from '../../components/task/TaskForm';
import Toast from '../../components/Toast';

// Define filter and sort options
type StatusFilter = 'all' | 'pending' | 'completed';
type SortOption = 'created_at' | '-created_at' | 'title' | '-title';

const TasksPage = () => {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [showForm, setShowForm] = useState<boolean>(false);
  const [statusFilter, setStatusFilter] = useState<StatusFilter>('all');
  const [sortOption, setSortOption] = useState<SortOption>('-created_at');
  const [page, setPage] = useState<number>(1);
  const [limit] = useState<number>(20); // Fixed limit per page
  const [toast, setToast] = useState<{ message: string; type: 'success' | 'error' | 'info' } | null>(null);

  // Check authentication on mount
  useEffect(() => {
    const token = localStorage.getItem('auth_token');
    if (!token) {
      window.location.href = '/login';
    }
  }, []);

  // Fetch tasks when filters change
  useEffect(() => {
    const fetchTasks = async () => {
      try {
        setLoading(true);
        const queryParams: { [key: string]: string | number } = {};

        if (statusFilter !== 'all') {
          queryParams.status = statusFilter;
        }
        if (sortOption) {
          queryParams.sort = sortOption;
        }
        queryParams.page = page;
        queryParams.limit = limit;

        const tasksData = await api.getTasks(queryParams);
        setTasks(tasksData);
      } catch (err) {
        setToast({ message: 'Failed to load tasks. Please try again.', type: 'error' });
        console.error('Error fetching tasks:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchTasks();
  }, [statusFilter, sortOption, page]);

  const handleTaskCreated = (newTask: Task) => {
    setTasks([newTask, ...tasks]); // Add new task to the beginning
    setToast({ message: 'Task created successfully!', type: 'success' });
    setShowForm(false);
  };

  const handleTaskUpdated = (updatedTask: Task) => {
    setTasks(tasks.map(task => task.id === updatedTask.id ? updatedTask : task));
    setToast({ message: 'Task updated successfully!', type: 'success' });
  };

  const handleTaskDeleted = (id: number) => {
    setTasks(tasks.filter(task => task.id !== id));
    setToast({ message: 'Task deleted successfully!', type: 'success' });
  };

  const handleToastClose = () => {
    setToast(null);
  };

  // Show loading state
  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 py-8">
        <div className="max-w-4xl mx-auto px-4">
          <div className="bg-white shadow rounded-lg p-6">
            <div className="animate-pulse flex space-x-4">
              <div className="flex-1 space-y-4 py-1">
                <div className="h-4 bg-gray-200 rounded w-3/4"></div>
                <div className="space-y-2">
                  <div className="h-4 bg-gray-200 rounded"></div>
                  <div className="h-4 bg-gray-200 rounded w-5/6"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-4xl mx-auto px-4">
        <div className="bg-white shadow rounded-lg p-6">
          <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-6 gap-4">
            <h1 className="text-2xl font-bold text-gray-800">My Tasks</h1>
            <div className="flex flex-wrap gap-3">
              <button
                onClick={() => setShowForm(!showForm)}
                className="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded-lg transition duration-200"
              >
                {showForm ? 'Cancel' : 'Add Task'}
              </button>

              {/* Filter Controls */}
              <select
                value={statusFilter}
                onChange={(e) => setStatusFilter(e.target.value as StatusFilter)}
                className="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="all">All Tasks</option>
                <option value="pending">Pending</option>
                <option value="completed">Completed</option>
              </select>

              {/* Sort Controls */}
              <select
                value={sortOption}
                onChange={(e) => setSortOption(e.target.value as SortOption)}
                className="px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
              >
                <option value="-created_at">Newest First</option>
                <option value="created_at">Oldest First</option>
                <option value="title">Title A-Z</option>
                <option value="-title">Title Z-A</option>
              </select>
            </div>
          </div>

          {/* Add new task form - conditionally rendered */}
          {showForm && (
            <TaskForm
              onTaskCreated={handleTaskCreated}
              onCancel={() => setShowForm(false)}
            />
          )}

          {/* Tasks list */}
          {tasks.length === 0 ? (
            <div className="text-center py-8">
              <p className="text-gray-500">No tasks found. {statusFilter !== 'all' ? 'Change your filters or ' : ''}add a new task to get started!</p>
            </div>
          ) : (
            <ul className="divide-y divide-gray-200">
              {tasks.map((task) => (
                <TaskItem
                  key={task.id}
                  task={task}
                  onUpdate={handleTaskUpdated}
                  onDelete={handleTaskDeleted}
                />
              ))}
            </ul>
          )}

          {/* Pagination controls */}
          <div className="flex justify-between items-center mt-6">
            <button
              onClick={() => setPage(Math.max(1, page - 1))}
              disabled={page <= 1}
              className={`px-4 py-2 rounded-lg ${
                page <= 1
                  ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
                  : 'bg-gray-500 hover:bg-gray-600 text-white'
              }`}
            >
              Previous
            </button>

            <span className="text-gray-600">
              Page {page}
              {tasks.length < limit && page === 1 ? '' : ` of ${tasks.length === limit ? 'many' : Math.ceil(tasks.length / limit)}`}
            </span>

            <button
              onClick={() => {
                if (tasks.length === limit) {
                  setPage(page + 1);
                }
              }}
              disabled={tasks.length < limit}
              className={`px-4 py-2 rounded-lg ${
                tasks.length < limit
                  ? 'bg-gray-200 text-gray-400 cursor-not-allowed'
                  : 'bg-gray-500 hover:bg-gray-600 text-white'
              }`}
            >
              Next
            </button>
          </div>
        </div>
      </div>
      {toast && <Toast message={toast.message} type={toast.type} onClose={handleToastClose} />}
    </div>
  );
};

export default TasksPage;