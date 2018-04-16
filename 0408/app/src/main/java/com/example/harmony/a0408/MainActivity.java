package com.example.harmony.a0408;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.view.View;
import android.widget.TextView;
public class MainActivity extends AppCompatActivity {
    private Button btndo;
    private EditText inputext;
    public String input;
    public TextView text;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btndo=(Button)findViewById(R.id.button);
        inputext=(EditText)findViewById(R.id.edit);
        text=(TextView)findViewById(R.id.textword);
        btndo.setOnClickListener(listener);
    }
    private Button.OnClickListener listener=new Button.OnClickListener(){
        @Override
        public void onClick(View v ){
        input=inputext.getText().toString();
        text.setText("你的學號是"+input);
        }
    };
}
