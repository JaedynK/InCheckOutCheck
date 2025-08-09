from lime.lime_tabular import LimeTabularExplainer
import numpy as np

def explain_with_lime(model, X_train, X_instance, feature_names, class_names, output_path="lime_explanation.txt"):
    explainer = LimeTabularExplainer(
        training_data=np.array(X_train),
        feature_names=feature_names,
        class_names=class_names,
        mode='classification'
    )

    explanation = explainer.explain_instance(X_instance, model.predict_proba)
    
    with open(output_path, "w") as f:
        f.write(str(explanation.as_list()))

    return explanation