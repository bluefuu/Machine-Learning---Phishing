import DecisionTree


class MLModel:
     dt = ""
     root_node = ""

     def __init__(self):
          #run model
          self.train()

     def train(self):
          training_data = "data/dataset.csv"
          self.dt = DecisionTree.DecisionTree(
                training_datafile = training_data,
                csv_class_column_index = 1,
                csv_columns_for_features = [2,3,4,5,6,7,8,9,10,11,12],
                entropy_threshold = 0.01,
                max_depth_desired = 8,
                symbolic_to_numeric_cardinality_threshold = 10,
                csv_cleanup_needed = 1,
          )

          self.dt.get_training_data()
          self.dt.calculate_first_order_probabilities()
          self.dt.calculate_class_priors()
          self.dt.show_training_data()
          self.root_node = self.dt.construct_decision_tree_classifier()
          self.root_node.display_decision_tree("   ")
          #sample = ['blacklist = 0', 'is_ipaddress = 0', 'is_at = 0', 'multi_domain = 0', 'url_length = 0', 'yg_domain = 0', 'bad_cookie = 0', 'foreign_links = 0', 'mismatch_favi = 1', 'no_dns = 0', 'bad_ssl = 0']
          
          #print(dt)

     def test(self, farray):
          result = self.dt.classify(self.root_node, farray)
          not_phishing = float(result.get('is_phishing=0'))
          is_phishing = float(result.get('is_phishing=1'))

          if not_phishing > 0.7:
               return "Safe"
          elif is_phishing > 0.7:
               return "Threat"
          else: 
               return "Unsure" 




