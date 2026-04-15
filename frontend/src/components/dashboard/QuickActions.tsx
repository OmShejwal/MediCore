import { motion } from "framer-motion";
import { Brain, ScanLine, MessageCircle, Dumbbell, Utensils, Pill } from "lucide-react";

const actions = [
  { icon: Brain, label: "AI Diagnosis", color: "bg-primary/10 text-primary hover:bg-primary/20" },
  { icon: ScanLine, label: "Body Scan", color: "bg-info/10 text-info hover:bg-info/20" },
  { icon: MessageCircle, label: "Health Coach", color: "bg-success/10 text-success hover:bg-success/20" },
  { icon: Dumbbell, label: "Workout", color: "bg-coral/10 text-coral hover:bg-coral/20" },
  { icon: Utensils, label: "Meal Plan", color: "bg-warning/10 text-warning hover:bg-warning/20" },
  { icon: Pill, label: "Medications", color: "bg-primary/10 text-primary hover:bg-primary/20" },
];

export function QuickActions() {
  return (
    <motion.div
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ delay: 0.15 }}
      className="grid grid-cols-3 sm:grid-cols-6 gap-3"
    >
      {actions.map((action) => (
        <button
          key={action.label}
          className={`flex flex-col items-center gap-2 p-4 rounded-xl border border-border transition-all hover:scale-105 hover:shadow-md ${action.color}`}
        >
          <action.icon className="h-5 w-5" />
          <span className="text-xs font-medium">{action.label}</span>
        </button>
      ))}
    </motion.div>
  );
}
